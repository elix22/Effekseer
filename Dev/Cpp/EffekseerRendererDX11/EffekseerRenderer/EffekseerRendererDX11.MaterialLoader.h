﻿
#ifndef __EFFEKSEERRENDERER_DX11_MATERIALLOADER_H__
#define __EFFEKSEERRENDERER_DX11_MATERIALLOADER_H__

#include "EffekseerRendererDX11.DeviceObject.h"
#include "EffekseerRendererDX11.RendererImplemented.h"
#include <memory>

namespace EffekseerRendererDX11
{

class MaterialLoader : public ::Effekseer::MaterialLoader
{
private:
	Renderer* renderer_ = nullptr;
	::Effekseer::FileInterface* fileInterface_ = nullptr;
	::Effekseer::DefaultFileInterface defaultFileInterface_;

public:
	MaterialLoader(Renderer* renderer, ::Effekseer::FileInterface* fileInterface);
	virtual ~MaterialLoader();

	::Effekseer::MaterialData* Load(const EFK_CHAR* path) override;

	::Effekseer::MaterialData* Load(const void* data, int32_t size) override;

	void Unload(::Effekseer::MaterialData* data) override;
};

} // namespace EffekseerRendererDX11

#endif // __EFFEKSEERRENDERER_GL_MODELLOADER_H__
