import bpy
psys = bpy.context.object.particle_systems.active.settings.mdl_particle_sys

psys.emitter_type = 'ParticleEmitter2'
psys.model_path = ''
psys.texture_path = 'Textures\\Flare.blp'
psys.filter_mode = 'Additive'
psys.emission_rate = 40
psys.life_span = 1.2000000476837158
psys.speed = 300
psys.gravity = 500.0
psys.longitude = 0.0
psys.latitude = 45
psys.ribbon_material = None
psys.ribbon_color = (1.0, 1.0, 1.0)
psys.variation = 0.5
psys.head = True
psys.tail = False
psys.tail_length = 0.0
psys.start_color = (0.21404114365577698, 0.002321986248716712, 0.002321986248716712)
psys.start_alpha = 180
psys.start_scale = 10
psys.mid_color = (0.3423916697502136, 0.1486983597278595, 0.002879259642213583)
psys.mid_alpha = 255
psys.mid_scale = 20
psys.end_color = (0.21404114365577698, 0.002321986248716712, 0.002321986248716712)
psys.end_alpha = 0
psys.end_scale = 10
psys.time = 0.30000001192092896
psys.rows = 1
psys.cols = 1
psys.head_life_start = 0
psys.head_life_end = 0
psys.head_life_repeat = 1
psys.head_decay_start = 0
psys.head_decay_end = 0
psys.head_decay_repeat = 1
psys.tail_life_start = 0
psys.tail_life_end = 0
psys.tail_life_repeat = 1
psys.tail_decay_start = 0
psys.tail_decay_end = 0
psys.tail_decay_repeat = 1
psys.unshaded = True
psys.unfogged = False
psys.line_emitter = False
psys.sort_far_z = False
psys.model_space = False
psys.xy_quad = False
