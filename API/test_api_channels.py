import pytest
from api_channels import Channels

channels = Channels()

@pytest.mark.api
def test_01_create_channel():
    channels.create_channel()

@pytest.mark.api
def test_02_check_channel_by_name():
    channels.check_channel_by_name()

@pytest.mark.api
def test_03_archive_channel_by_id():
    channels.archive_channel_by_id()

@pytest.mark.api
def test_04_delete_channel_by_id():
    channels.delete_channel_by_id()