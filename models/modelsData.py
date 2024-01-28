#title, desc, github, runs
class Image:
    
    prompts = {
	 "colors": ['autochrome', 'cinecolour', 'colour', 'colourised', 'colour wheel',
			  'cyanopsia', 'faded', 'faded colours', 'high contrast', 'hue',
			  'low contrast', 'kinemacolour', 'kodachrome', 'monochromatic', 'monochrome',
			  'neon', 'neonpink', 'pigment', 'pure', 'sepia',
			  'spectrum', 'technicolor', 'tone', 'triadic colours', 'variegated',
			  'vibrant'],
	"lighting": ['artificial lighting', 'backlight', 'bright', 'bubble light', 'crepuscular rays',
			   'dark lighting', 'dynamic lighting', 'flickering light', 'floodlight', 'frontlight',
			   'moonlight', 'natural lighting', 'soft lighting', 'spotlight', 'strobe',
			   'strobe light', 'sunlight', 'vivid lighting'],
	"details": ['8k', 'concept art', 'highly detailed', 'hyperrealism',
		'hyperrealistic', 'insanely detailed', 'octane render', 'perfect composition',
		'photorealism', 'photorealistic', 'unreal engine'],
	"artists": ['anne stokes']
    }
    
    sdxl = {"author":"stability-ai", "model":"sdxl", "desc":"A text-to-image generative AI model that creates beautiful images","github":"https://github.com/replicate/cog-sdxl","runs":"33.4M"}
    
    stable_diff = {"author":"stability-ai", "model":"stable-diffusion", "desc":"A latent text-to-image diffusion model capable of generating photo-realistic images given any text input","github":"https://github.com/replicate/cog-stable-diffusion","runs":"106.5M"}
    
    kandinsky = {"author":"ai-forever", "model":"kandinsky-2.2", "desc":"multilingual text2image latent diffusion model","github":"https://github.com/chenxwh/Kandinsky-2/tree/v2.2","runs":"7.1M"}
    

class Text:
    llama70 = {"author":"meta", "model":"llama-2-70b-chat", "desc":"A 70 billion parameter language model from Meta, fine tuned for chat completions","github":"https://github.com/a16z-infra/cog-llama-template","runs":"4.3M"}