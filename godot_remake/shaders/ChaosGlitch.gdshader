shader_type canvas_item;

uniform float glitch_strength : hint_range(0.0, 1.0) = 0.1;
uniform float trigger : hint_range(0.0, 1.0) = 0.0; // Set to > 0.9 via script to trigger glitch

float random(vec2 uv) {
    return fract(sin(dot(uv, vec2(12.9898, 78.233))) * 43758.5453123);
}

void fragment() {
    vec2 uv = UV;

    if (trigger > 0.0) {
        float time_snap = floor(TIME * 15.0);
        if (random(vec2(time_snap, time_snap)) > 0.8) {
            float shift = random(vec2(time_snap, uv.y)) * glitch_strength;
            uv.x += shift - (glitch_strength * 0.5);

            vec4 col;
            col.r = texture(TEXTURE, uv + vec2(0.01, 0.0)).r;
            col.g = texture(TEXTURE, uv).g;
            col.b = texture(TEXTURE, uv - vec2(0.01, 0.0)).b;
            col.a = texture(TEXTURE, uv).a;
            COLOR = col;
        } else {
            COLOR = texture(TEXTURE, uv);
        }
    } else {
        COLOR = texture(TEXTURE, uv);
    }
}
