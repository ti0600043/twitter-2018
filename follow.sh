#!/bin/sh

echo "開始：" `date "+%Y%m%d_%H%M%S"`

python follow_002.py
python follow_003.py

echo "終了：" `date "+%Y%m%d_%H%M%S"`
