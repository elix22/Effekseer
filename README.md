﻿Effekseer
=========
This software is a tool editing particle effects.
By incorporating a runtime and plug-ins, you will be able to show the effects that was created with Effekseer.
Effekseer is useful in developing game software especially. Not only programmers but also designers take charge of particle effects.

* [Official website](http://effekseer.github.io/en/)

本ソフトウェアはパーティクルエフェクト編集ツールです。
ランタイムやプラグインを組み込むことで、Effekseerで作成されたエフェクトをアプリケーション中で再生できるようになります。
主にゲームで使用することを想定しており、パーティクルエフェクトの編集をプログラマでなくデザイナーが担当できるようにします。

* [公式ウェブサイト](http://effekseer.github.io/jp/)

本軟件為粒子效果的編輯工具。
透過組合 runtime 和插件,由Effekseer制作而成的效果便可以在應用程式內播放。
Effekseer主要用作遊戲開發,不僅是程序員而且設計師也可進行粒子效果的編輯。

* [Official website](http://effekseer.github.io/en/)

[![Slack Status](https://effekseer-slackin.herokuapp.com/badge.svg)](https://effekseer-slackin.herokuapp.com/)

[![](http://img.youtube.com/vi/WwNX9TO7guA/0.jpg)](https://www.youtube.com/watch?v=WwNX9TO7guA)

* [ForUnity](https://github.com/effekseer/EffekseerForUnity)

* [ForUE4](https://github.com/effekseer/EffekseerForUE4)

* [ForCocos2d-x](https://github.com/effekseer/EffekseerForCocos2d-x)

* [ForDXLib](https://github.com/effekseer/EffekseerForDXLib)

* [ToolHelp(Sphinx)](https://github.com/effekseer/docs_tool)

Development
=========

### Branch

* master 1.6(WIP)

* [1.5x](https://github.com/effekseer/Effekseer/tree/15x)

* [1.4x](https://github.com/effekseer/Effekseer/tree/14x)

* [1.3x](https://github.com/effekseer/Effekseer/tree/13x)

### Documents

[CodeOverview](docs/Development/CodeOverview.md)

[CodingRule](docs/Development/CodingRule_En.md)

[HowToBuild](docs/Development/HowToBuild.md)

[コーディングルール](docs/Development/CodingRule_Ja.md)

Todo
=========

Please read issues, Trello and TODO. We always welcome pull requests for improvements, bug fixes, and so on.

issues、TrelloとTODOを読んでください。常時、機能追加、バグ修正といったプルリクエストを募集しております。

[Issues](https://github.com/effekseer/Effekseer/issues)

[Trello](https://trello.com/b/APLk8e6V/effekseer-wishlist)

# RoadMap

- I'm planning.

## OnGoing

- Support Metal
- Support Vulkan

[BackendRepository](https://github.com/altseed/LLGI)

# Todo

## Easy

- Add samples (サンプルの追加)
- Add tutorial documents (チュートリアルのドキュメントの追加)
- Add tests for a runtime (ランタイムのテストの追加)
- Translate documents from Japanese into English (ドキュメントの日本語から英語への翻訳)

## Medium
- Add model exporters for 3D modeling softwares

## Hard

- Support AfterEffects

## Others
- New method of rotation to match Z and moving direction.

# For contributor

## How to release (under constructing)

* Windows

Visual Studio 2017 are required.

Open ```release.bat```

* Mac

Execute ```Dev/build.Mac.sh``` to compile and generate binary into Dev/release/

Execute ```Dev/package.Mac.sh``` to generate app into Dev/Mac/

or

Use cmake to ```Dev/Cpp/CMakeLists.txt```

* Linux (not work now)

Execute ```Dev/build.Linux.sh``` to compile and generate binary into Dev/release/

I have not debuged Effekseer on Linux yet.
