#!/bin/sh

echo "開始：" `date "+%Y%m%d_%H%M%S"`

python follow_002.py 2>&1 | tee follow_002.log
python follow_003.py 2>&1 | tee follow_003.log

echo "終了：" `date "+%Y%m%d_%H%M%S"`
