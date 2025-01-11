#!/usr/bin/env bash
PROJECT_DIR=$(realpath $(dirname $BASHSOURCE[0]))
source $PROJECT_DIR/scripts/colours.sh
printf "${CC_BOLD}Building project: ${CC_BLUE}%s${CC_NONE}\n" $PROJECT_DIR
printf "\tBuild with uv:        ${CC_CYAN}uv build${CC_NONE}\n"
uv build --quiet
if [ $? -ne 0 ]; then
    printf "${CC_BOLD_RED}Build failed${CC_NONE}\n"
    exit 1
fi
printf "\tInstall with uv:      ${CC_CYAN}uv pip install .${CC_NONE}\n"
uv pip install -qe .
if [ $? -ne 0 ]; then
    printf "${CC_BOLD_RED}Build failed${CC_NONE}\n"
    exit 1
fi
printf "${CC_BOLD_GREEN}Build successful${CC_NONE}\n"
