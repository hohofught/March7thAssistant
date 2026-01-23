from ..card.messagebox_custom import MessageBoxDisclaimer
from module.config import cfg
import markdown
import base64
import sys
import os
from module.localization import tr


def disclaimer(self):
    html_style = """
<style>
a {
    color: #f18cb9;
    font-weight: bold;
}
</style>
"""
    try:
        dialog = MessageBoxDisclaimer(tr("DisclaimerTitle"),html_style + markdown.markdown(tr("DisclaimerContent")),self.window())
        result = dialog.exec()
        if result:
            sys.exit(0)
        cfg.set_value(base64.b64decode("YXV0b191cGRhdGU=").decode("utf-8"), True)
        if sys.platform == 'win32':
            path = os.path.join(os.environ[base64.b64decode("UHJvZ3JhbURhdGE=").decode("utf-8")],base64.b64decode("TWFyY2g3dGhBc3Npc3RhbnQvZGlzY2xhaW1lcg==").decode("utf-8"))
        else:
            path = os.path.join(os.path.expanduser("~"),base64.b64decode("Lm1hcmNoN3RoYXNzaXN0YW50L2Rpc2NsYWltZXI=").decode("utf-8"))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, 'a').close()
    except Exception:
        sys.exit(0)
