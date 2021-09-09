import os
import pytest


@pytest.mark.skipif(pytest.skip_torch, reason="requires pytorch")
def test_torchscript_converter(unet2d_nuclei_broad_model, tmp_path):
    from bioimageio.core.weight_converter.torch import convert_weights_to_pytorch_script

    out_path = tmp_path / "weights.pt"
    convert_weights_to_pytorch_script(unet2d_nuclei_broad_model, out_path)
    assert os.path.exists(out_path)
    # TODO check results for correctness