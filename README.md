# 不着边际的心理

一个温柔的艺术与日常放松小角落。奶油白、鼠尾草绿和浅桃色，搭配低透明度纸纹与主题插画。

## 网站

部署成功后访问：https://lijiayangzi922-ship-it.github.io/borderless-mind/

20 个内容页面，包含绘画、声音、呼吸练习与心情手帐。登录、留言和手帐为浏览器本地演示功能，没有服务器账户系统。

## 完整源码

为便于传输，完整网站文件存放在 `site-source.zip.part01` 至 `part21` 中，清单与 SHA-256 校验值位于 `source-manifest.json`。

下载仓库全部文件后运行 `python3 expand-site.py`，即可校验并将全部可编辑 HTML、CSS、JS、字体、图片和视频还原到 `_site` 目录。直接打开 `_site/index.html` 即可本地浏览。

## 发布

GitHub Actions 在源码清单更新或手动触发时，校验分卷、还原网站并部署到 GitHub Pages。部署使用 HTTPS。

素材来源与许可位于还原后的网站 `docs/media-sources.html` 和 `fonts/OFL.txt`。参考图片仅用于风格参考，未直接插入网站。网站中的机构与课程信息为虚拟设计示意。
