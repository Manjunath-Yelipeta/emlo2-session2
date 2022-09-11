import pyrootutils

root = pyrootutils.setup_root(
    search_from=__file__,
    indicator=[".git", "pyproject.toml"],
    pythonpath=True,
    dotenv=True,
)
from typing import List, Optional, Tuple

import hydra
from omegaconf import DictConfig

@hydra.main(version_base="1.2", config_path=root / "configs", config_name="test.yaml")
def main(cfg: DictConfig) -> Optional[float]:
    print(cfg)
    dm = hydra.utils.instantiate(cfg)
    print(dm())
if __name__ == "__main__":
    main()

