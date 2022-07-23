#
# Copyright (C) 2021-2022 by Buzz@Github, < https://github.com/justteen >.
#
# This file is part of < https://github.com/justteen/musicalbuzz > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/justteen/musicalbuzz/blob/main/LICENSE >
#
# All rights reserved.

class AssistantErr(Exception):
    def __init__(self, errr: str):
        super().__init__(errr)
