import torch

from shap_e.diffusion.sample import sample_latents
from shap_e.diffusion.gaussian_diffusion import diffusion_from_config
from shap_e.models.download import load_model, load_config
from shap_e.util.image_util import load_image
from shap_e.util.notebooks import decode_latent_mesh

def generate_mesh_from_image():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    xm = load_model('transmitter', device=device)
    model = load_model('image300M', device=device)
    diffusion = diffusion_from_config(load_config('diffusion'))
    
    batch_size = 4
    guidance_scale = 3.0

    image = load_image("PATH_0F_.obj_FILE")

    latents = sample_latents(
        batch_size=batch_size,
        model=model,
        diffusion=diffusion,
        guidance_scale=guidance_scale,
        model_kwargs=dict(images=[image] * batch_size),
        progress=True,
        clip_denoised=True,
        use_fp16=True,
        use_karras=True,
        karras_steps=128,
        sigma_min=1e-1,
        sigma_max=160,
        s_churn=0,
    )


    for i, latent in enumerate(latents):
        t = decode_latent_mesh(xm, latent).tri_mesh()
        with open(f'chair_{i}.obj', 'w') as f:
            t.write_obj(f)

if __name__ == '__main__':
    generate_mesh_from_image()
