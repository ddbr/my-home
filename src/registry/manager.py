import yaml

def load_registry(path="config/registry.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def get_scene(scene_id, registry):
    return registry["scenes"].get(str(scene_id))
