from models.image.aiforever import kandinsky
from models.image.stabilityai import sdxl, stablediffusion
from models.image.fofr import latent_consistency_model
from models.image.anything import anythingv5
from models.image.lykon import dreamshaper8, absolutereality
from models.image.rqdwdw import counterfeitv3
from models.image.lostdog import am_i_real
from models.image.wrs111 import guofeng3
from models.image.kandooai import juggernaut_aftermath
from models.image.bradcatt import toonyou6
from models.image.prompthero import openjourneyv4

from models.video.lucataco import animatediff
from models.video.anotherjesse import zeroscopev2xl
from models.video.stabilityai import stable_video_diffusion

from models.text.mistralai import mistral7
from models.text.meta import llama70, codellama

from flask import jsonify

def get_model(prompt, model, neg_prompt=None, seed=None, cfg=None, steps=None):
    
    #test model
    
    if model == "test":
        return jsonify({"response":"hello from chipling!"})
    
    #image models
    
    elif model == "stability-ai/sdxl":
        data = sdxl.sdxl.create_image(prompt)
        return jsonify(data)

    elif model == "ai-forever/kandinsky-2.2":
        data = kandinsky.kandisky.create_image(prompt)
        return jsonify(data)

    elif model == "stability-ai/stable-diffusion":
        data = stablediffusion.stablediff.create_image(prompt)
        return jsonify(data)
    
    elif model == "fofr/latent-consistency-model":
        data = latent_consistency_model.latentConsistency.create_image(prompt)
        return jsonify(data)    
    
    #text models
    
    elif model == "meta/llama-2-70b-chat":
        data  = llama70.llama70.create_req(prompt)
        return jsonify(data)
    
    elif model == "mistralai/mistral-7b-instruct-v0.1":
        data = mistral7.Mistral7b.create_req(prompt)
        return jsonify(data)
    
    #video models
    elif model == "lucataco/animate-diff":
        data = animatediff.animateDiff.create_vid(prompt)
        return jsonify(data)
    
    elif model == "anotherjesse/zeroscope-v2-xl":
        data = zeroscopev2xl.zeroScope.create_vid(prompt)
        return jsonify(data)
    
    elif model == "meta/codellama-13b":
        data  = codellama.codeLlama13B.create_req(prompt)
        return jsonify(data)
    
    elif model == "anything/anythingv5":
        data = anythingv5.anythingv5.create_image(prompt=prompt, neg_prompt=neg_prompt, seed=seed, cfg=cfg, steps=steps)
        return jsonify(data)
    
    elif model == "lykon/dreamshaper8":
        data = dreamshaper8.dreamshaper.create_image(prompt=prompt, neg_prompt=neg_prompt, seed=seed, cfg=cfg, steps=steps)
        return jsonify(data)
    
    elif model == "lykon/absolutereality":
        data = absolutereality.absoluteReality.create_image(prompt=prompt, neg_prompt=neg_prompt, seed=seed, cfg=cfg, steps=steps)
        return jsonify(data)
    
    elif model == "stability-ai/stable-video-diffusion":
        data = stable_video_diffusion.stablevideoDiff.create_vid(prompt)
        return jsonify(data)
    
    elif model == "rqdwdw/counterfeitv3":
        data = counterfeitv3.counterFeitv3.create_image(prompt=prompt, neg_prompt=neg_prompt, seed=seed, cfg=cfg, steps=steps)
        return jsonify(data)
    
    elif model == "lostdog/am-i-real":
        data = am_i_real.amiReal.create_image(prompt=prompt, neg_prompt=neg_prompt, seed=seed, cfg=cfg, steps=steps)
        return jsonify(data)
    
    elif model == "wrs111/guofeng3":
        data = guofeng3.guoFeng3.create_image(prompt=prompt, neg_prompt=neg_prompt, seed=seed, cfg=cfg, steps=steps)
        return jsonify(data)
    
    elif model == "kandooai/juggernaut_aftermath":
        data = juggernaut_aftermath.juggernautAftermath.create_image(prompt=prompt, neg_prompt=neg_prompt, seed=seed, cfg=cfg, steps=steps)
        return jsonify(data)
    
    elif model == "bradcatt/toonyou6":
        data = toonyou6.toonYou6.create_image(prompt=prompt, neg_prompt=neg_prompt, seed=seed, cfg=cfg, steps=steps)
        return jsonify(data)
    
    elif model == "prompthero/openjourneyv4":
        data = openjourneyv4.openJourneyv4.create_image(prompt=prompt, neg_prompt=neg_prompt, seed=seed, cfg=cfg, steps=steps)
        return jsonify(data)

    else:
        return jsonify({"error": "error occurred"})