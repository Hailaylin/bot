path = '~'


def help():
    return f'''{path}ab - 查看Minecraft Wiki过滤器日志。
{path}bug <JiraID> - 从Mojira中获取此Bug的信息。
{path}credits - 展示制作人员列表。
{path}mcv - 获取当前Minecraft Java版最新版本。
{path}mcbv - 获取当前Minecraft基岩版最新版本。
{path}mcdv - 获取当前Minecraft Dungeons最新版本。
{path}rc - 查看Minecraft Wiki最近更改。
{path}server -h
{path}user -h
{path}wiki -h
! - 用于快捷查bug，如!mc-4
[[]] - 用于快捷查wiki，如[[海晶石]]
{{{{}}}} - 用于快捷查wiki模板，如{{{{v}}}}
[30秒后撤回本消息]'''


def wikihelp():
    return f'''{path}wiki ~<site> <pagename> - 从指定Gamepedia站点中输出条目链接。
{path}wiki <lang>:<pagename>, {path}wiki-<lang> <pagename> - 从指定语言中的Minecraft Wiki中输出条目链接。
{path}wiki <pagename> - 从Minecraft Wiki（英文）中输出条目链接。'''


def userhelp():
    return f'''{path}user ~<site> <pagename> - 从指定Gamepedia站点中输出用户信息。
{path}user <lang>:<pagename>, {path}user-<lang> <pagename> - 从指定语言中的Minecraft Wiki中输出用户信息。
{path}user <pagename> - 从Minecraft Wiki（英文）中输出用户信息。
[-r] - 输出详细信息。
[-p] - 输出一张用户信息的图片（不包含用户组）。'''

def credits():
    return '''===============
主开发者    OasisAkari

                 _LittleC_
代码贡献    Dianliang233
                 wyapx
2020 Teahouse Studios
===============
此机器人的源代码已于https://github.com/Teahouse-Studios/bot仓库与母项目Graia采用相同协议AGPL-3.0 License进行开源。
[30秒后撤回本消息]'''