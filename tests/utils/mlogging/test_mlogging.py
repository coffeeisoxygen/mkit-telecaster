import asyncio

import pytest
from app.utils.mlogging.decorators import log_entry_exit, log_exec_time, timeit
from loguru import logger


@pytest.fixture(autouse=True)
def setup_loguru(tmp_path, monkeypatch):
    # Redirect loguru logs to a file for assertion
    log_file = tmp_path / "loguru_test.log"
    logger.remove()
    logger.add(log_file, format="{message}")
    yield log_file
    logger.remove()
    logger.add(lambda msg: None)  # Silence after test


def test_log_entry_exit_sync(setup_loguru):
    @log_entry_exit(entry=True, exit=True, level="INFO")
    def foo(x):
        return x + 1

    result = foo(1)
    assert result == 2
    log_content = setup_loguru.read_text()
    assert "Entering 'foo'" in log_content
    assert "Exiting 'foo'" in log_content


@pytest.mark.asyncio
async def test_log_entry_exit_async(setup_loguru):
    @log_entry_exit(entry=True, exit=True, level="INFO")
    async def bar(x):
        await asyncio.sleep(0)
        return x * 2

    result = await bar(3)
    assert result == 6
    log_content = setup_loguru.read_text()
    assert "Entering 'bar'" in log_content
    assert "Exiting 'bar'" in log_content


def test_log_exec_time_sync(setup_loguru):
    @log_exec_time(entry=True, exit=True, level="INFO")
    def foo(x):
        return x + 2

    result = foo(2)
    assert result == 4
    log_content = setup_loguru.read_text()
    assert "Execution time for 'foo'" in log_content


@pytest.mark.asyncio
async def test_log_exec_time_async(setup_loguru):
    @log_exec_time(entry=True, exit=True, level="INFO")
    async def bar(x):
        await asyncio.sleep(0)
        return x * 3

    result = await bar(2)
    assert result == 6
    log_content = setup_loguru.read_text()
    assert "Execution time for 'bar'" in log_content


def test_timeit_decorator(setup_loguru):
    @timeit
    def foo(x):
        return x * 5

    result = foo(2)
    assert result == 10
    log_content = setup_loguru.read_text()
    assert "executed in" in log_content
