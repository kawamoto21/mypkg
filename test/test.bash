#!/bin/bash
# SPDX-FileCopyrightText: 2025 Sou Kawamoto <s23c1040mc@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause

# ホームディレクトリを変更可能にする設定
dir=~
[ "$1" != "" ] && dir="$1"

# 作業ディレクトリの変更
cd $dir/ros2_ws || { echo "ディレクトリ $dir/ros2_ws に移動できません"; exit 1; }

# ROS 2のワークスペースをビルド
colcon build || { echo "ビルドに失敗しました"; exit 1; }

# ROS 2環境をソース
source install/setup.bash || { echo "ROS 2 環境のセットアップに失敗しました"; exit 1; }

# ノードを直接起動して動作確認を実行
# `timeout` コマンドで10秒間の動作を確認
timeout 10 bash -c "
    python3 src/mypkg/talker.py &
    talker_pid=\$!
    python3 src/mypkg/listener.py &
    listener_pid=\$!
    wait \$talker_pid \$listener_pid
" > /tmp/mypkg.log || { echo "ノード実行に失敗しました"; exit 1; }

# ログに含まれる内容を確認
if grep -q 'Count: 10' /tmp/mypkg.log; then
    echo "Test Passed: ログに指定のメッセージが含まれています"
else
    echo "Test Failed: 指定のメッセージがログにありません"
    exit 1
fi

