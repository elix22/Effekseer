import re

class CreateHeader:
	def __init__(self):
		self.lines = []

	def readLines(self,path):
		f = open(path)
		line = f.readline()
		while line:
			if re.search('include \"', line) == None:
 	 			self.lines.append(line)
    			line = f.readline()
		f.close

	def output(self,path):
		f = open(path, 'w')
		for line in self.lines:
			f.write(line)
		f.close()


effekseerHeader = CreateHeader()
effekseerHeader.readLines('Effekseer/Effekseer/Effekseer.Base.Pre.h')
effekseerHeader.readLines('Effekseer/Effekseer/Effekseer.Vector2D.h')
effekseerHeader.readLines('Effekseer/Effekseer/Effekseer.Vector3D.h')
effekseerHeader.readLines('Effekseer/Effekseer/Effekseer.Color.h')
effekseerHeader.readLines('Effekseer/Effekseer/Effekseer.RectF.h')
effekseerHeader.readLines('Effekseer/Effekseer/Effekseer.Matrix43.h')
effekseerHeader.readLines('Effekseer/Effekseer/Effekseer.Matrix44.h')
effekseerHeader.readLines('Effekseer/Effekseer/Effekseer.File.h')
effekseerHeader.readLines('Effekseer/Effekseer/Effekseer.DefaultFile.h')
effekseerHeader.readLines('Effekseer/Effekseer/Effekseer.Effect.h')
effekseerHeader.readLines('Effekseer/Effekseer/Effekseer.Manager.h')

effekseerHeader.readLines('Effekseer/Effekseer/Renderer/Effekseer.SpriteRenderer.h')
effekseerHeader.readLines('Effekseer/Effekseer/Renderer/Effekseer.RibbonRenderer.h')
effekseerHeader.readLines('Effekseer/Effekseer/Renderer/Effekseer.RingRenderer.h')
effekseerHeader.readLines('Effekseer/Effekseer/Renderer/Effekseer.ModelRenderer.h')
effekseerHeader.readLines('Effekseer/Effekseer/Renderer/Effekseer.TrackRenderer.h')

effekseerHeader.readLines('Effekseer/Effekseer/Effekseer.EffectLoader.h')
effekseerHeader.readLines('Effekseer/Effekseer/Effekseer.TextureLoader.h')
effekseerHeader.readLines('Effekseer/Effekseer/Effekseer.ModelLoader.h')

effekseerHeader.readLines('Effekseer/Effekseer/Effekseer.Model.h')

effekseerHeader.readLines('Effekseer/Effekseer/Sound/Effekseer.SoundPlayer.h')

effekseerHeader.readLines('Effekseer/Effekseer/Effekseer.SoundLoader.h')

effekseerHeader.readLines('Effekseer/Effekseer/Effekseer.Server.h')
effekseerHeader.readLines('Effekseer/Effekseer/Effekseer.Client.h')

effekseerHeader.readLines('Effekseer/Effekseer/Effekseer.CriticalSection.h')
effekseerHeader.readLines('Effekseer/Effekseer/Effekseer.Thread.h')

effekseerHeader.output('Effekseer/Effekseer.h')

effekseerRendererDX9Header = CreateHeader()
effekseerRendererDX9Header.readLines('EffekseerRendererDX9/EffekseerRenderer/EffekseerRenderer.Base.Pre.h')
effekseerRendererDX9Header.readLines('EffekseerRendererDX9/EffekseerRenderer/EffekseerRenderer.Renderer.h')
effekseerRendererDX9Header.output('EffekseerRendererDX9/EffekseerRendererDX9.h')

effekseerRendererDX11Header = CreateHeader()
effekseerRendererDX11Header.readLines('EffekseerRendererDX11/EffekseerRenderer/EffekseerRenderer.Base.Pre.h')
effekseerRendererDX11Header.readLines('EffekseerRendererDX11/EffekseerRenderer/EffekseerRenderer.Renderer.h')
effekseerRendererDX11Header.output('EffekseerRendererDX11/EffekseerRendererDX11.h')

effekseerRendererGLHeader = CreateHeader()
effekseerRendererGLHeader.readLines('EffekseerRendererGL/EffekseerRenderer/EffekseerRenderer.Base.Pre.h')
effekseerRendererGLHeader.readLines('EffekseerRendererGL/EffekseerRenderer/EffekseerRenderer.Renderer.h')
effekseerRendererGLHeader.output('EffekseerRendererGL/EffekseerRendererGL.h')