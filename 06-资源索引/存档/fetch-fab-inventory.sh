#!/bin/zsh
# ============================================================
# Fab Lab 官方设备清单一键存档脚本
# 说明：inventory.fabcloud.io 与 gitlab.fabcloud.org 共用同一台
#       GitLab 服务器，故障时会同时 502（"Waiting for GitLab to boot"）。
#       本脚本周期性探测，恢复后自动抓取 3 种格式存档。
# 用法：./fetch-fab-inventory.sh   （可选加参数 --wait 开启自动重试等待）
# 依赖：curl
# ============================================================

BASE="https://gitlab.fabcloud.org/inventory/inventory.fabcloud.io/-/raw/main/public"
DEST="$(cd "$(dirname "$0")" && pwd)"
FILES=(inv.toml inv.json inv.xlsx)

echo "存档目录: $DEST"

probe() {
  curl -s -o /dev/null -w "%{http_code}" -m 10 "$BASE/inv.toml"
}

fetch_all() {
  echo "=== 服务已恢复，开始下载 ==="
  for f in "${FILES[@]}"; do
    if curl -sL -m 60 -o "$DEST/$f" "$BASE/$f" && [ -s "$DEST/$f" ]; then
      echo "  ✓ $f  ($(wc -c < "$DEST/$f" | tr -d ' ') bytes)"
    else
      echo "  ✗ $f 下载失败"
    fi
  done
  echo "=== 完成：文件已保存到 $DEST ==="
}

if [ "$1" = "--wait" ]; then
  echo "探测中...（每 30 秒一次）"
  for i in {1..120}; do
    code=$(probe)
    echo "  [$i] HTTP $code  $(date +%H:%M:%S)"
    if [ "$code" = "200" ]; then
      fetch_all
      exit 0
    fi
    sleep 30
  done
  echo "等待超时（60 分钟），请稍后重跑本脚本。"
else
  code=$(probe)
  echo "当前状态: HTTP $code"
  if [ "$code" = "200" ]; then
    fetch_all
  else
    echo "服务尚未恢复（502 = GitLab 重启中）。"
    echo "可重跑: $0 --wait   （自动等待并抓取）"
    exit 1
  fi
fi
