import io
import shutil
from unittest.mock import patch

import requests


def test_labelary_example(tmp_path):
    zpl = "^XA^XZ"
    url = 'http://api.labelary.com/v1/printers/8dpmm/labels/4x6/0/'
    files = {'file': zpl}
    headers = {'Accept': 'application/pdf'}
    fake_pdf = b'%PDF-1.4\n%Fake PDF\n'

    class FakeResponse:
        def __init__(self, content, status_code=200):
            self.status_code = status_code
            self.raw = io.BytesIO(content)
            self.text = ''

    with patch('requests.post', return_value=FakeResponse(fake_pdf)) as mock_post:
        response = requests.post(url, headers=headers, files=files, stream=True)
        assert response.status_code == 200
        response.raw.decode_content = True
        output_file = tmp_path / 'label.pdf'
        with open(output_file, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        assert output_file.read_bytes() == fake_pdf
        mock_post.assert_called_once_with(url, headers=headers, files=files, stream=True)
