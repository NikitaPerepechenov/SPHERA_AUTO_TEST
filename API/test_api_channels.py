from api_channels import Channels
import pytest

channels = Channels()

@pytest.mark.api
def test_01_create_channel():
    channels.create_channel()

@pytest.mark.api
def test_02_check_channel_by_name():
    channels.check_channel_by_name()

@pytest.mark.api
def test_03_delete_channel_by_id():
    channels.delete_channel_by_id()