# Changelog

本项目的显著变更记录在此。格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，
版本号遵循 [SemVer](https://semver.org/lang/zh-CN/)。

## [1.0.0] - 2026-10-28

### Added
- WebHID 控制台，替代原厂 Windows 软件「B52Nano 设置工具 v1.3」
  - 蓝牙控制：配对 / 回连 / 断开 / 锁定 / 解锁
  - 适配器信息：型号、固件版本、耳机连接状态、当前编码
  - 高级设置：aptX / aptX HD / aptX LL / aptX Adaptive 编码开关、
    aptX Adaptive 音质⇄低延时模式、自动切换蓝牙音频、重启自动配对
  - 一键「推荐设置」（全部编码开启，修复出厂仅 SBC 的问题）
  - Chrome 音频输出选择与左右声道测试音
  - 实时 HID 协议日志与耳机多媒体按键转发显示
  - `?selftest` 无头自测模式（帧构造与应答解析断言）
- 完整协议文档（逆向自原厂工具，真机逐条验证）：[docs/protocol.md](docs/protocol.md)
- 本地启动器 `serve.py` 与 Linux udev 权限说明
