import io
from unittest.mock import patch

from zpl_to_pdf.generate import convert_zpl_to_pdf


def test_labelary_example(tmp_path):
    zpl = "^XA^XZ"
    url = 'http://api.labelary.com/v1/printers/12dpmm/labels/4x6/0/'
    fake_pdf = b'%PDF-1.4\n%Fake PDF\n'

    class FakeResponse:
        def __init__(self, content, status_code=200):
            self.status_code = status_code
            self.raw = io.BytesIO(content)
            self.text = ''

    output_file = tmp_path / 'label.pdf'

    with patch('requests.post', return_value=FakeResponse(fake_pdf)) as mock_post:
        convert_zpl_to_pdf(zpl, output_file)
        assert output_file.read_bytes() == fake_pdf
        mock_post.assert_called_once_with(
            url,
            headers={'Accept': 'application/pdf'},
            files={'file': zpl},
            stream=True,
        )
