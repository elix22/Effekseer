#version 450
#extension GL_ARB_separate_shader_objects : enable

layout(location = 0) in vec4 vaColor;
layout(location = 1) in vec4 vaTexCoord;

layout(location = 0) out vec4 o_Color;

void main()
{
	o_Color = vaColor;
}
