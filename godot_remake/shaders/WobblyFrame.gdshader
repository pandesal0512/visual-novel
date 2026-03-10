shader_type canvas_item;

uniform float strength : hint_range(0.0, 0.1) = 0.005;
uniform float frequency : hint_range(0.0, 50.0) = 10.0;
uniform float speed : hint_range(0.0, 10.0) = 2.0;

void fragment() {
    vec2 uv = UV;
    float wave_x = sin(uv.y * frequency + TIME * speed) * strength;
    float wave_y = cos(uv.x * frequency + TIME * speed) * strength;
    uv.x += wave_x;
    uv.y += wave_y;
    COLOR = texture(TEXTURE, uv);
}
