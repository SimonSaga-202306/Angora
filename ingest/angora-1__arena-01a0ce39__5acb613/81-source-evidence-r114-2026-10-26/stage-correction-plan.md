# 首次精确暂存前检查偏差及纠正计划

首次生成暂存清单后核对工作区时，发现 8 个 `tools/__pycache__/*.pyc` 是本轮 Python 单元测试和验证导入生成的临时字节码，不属于交付物。检查按预期停止，**尚未执行 git add**。不将这些缓存暂存或当作来源。

先保留第一次 `stage-paths.txt` 和 `output-manifest-before-stage.csv` 的快照，记录其为已过时的第一轮尝试；然后仅逐一删除这八个本轮测试生成的、已具名的 `.pyc` 文件，不执行 `git clean`、不动其他文件或目录。此后使用 `PYTHONDONTWRITEBYTECODE=1` 运行 Python。重新逐文件生成清单和清单哈希，包括这份纠正计划和第一轮记录，再核对工作区与清单完全一致；只有匹配后才暂存。

目标字节码 basename：`test_verify_r111.cpython-311.pyc`、`test_verify_r112.cpython-311.pyc`、`test_verify_r113.cpython-311.pyc`、`test_verify_r114.cpython-311.pyc`、`verify_r111.cpython-311.pyc`、`verify_r112.cpython-311.pyc`、`verify_r113.cpython-311.pyc`、`verify_r114.cpython-311.pyc`。这些仅是可再生成缓存，不是用户素材、研究正文或 Git 对象。
