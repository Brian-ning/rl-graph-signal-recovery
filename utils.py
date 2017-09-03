import json
from networkx.readwrite import json_graph

class ObjectEncoder(json.JSONEncoder):
  def default(self, obj):
    if hasattr(obj, "to_json"):
      return self.default(obj.to_json())
    if isinstance(obj, set):
      return list(obj)
    return json.JSONEncoder.default(self, obj)

DEFAULT_JSON_ARGS = {
  "indent": 2,
  "separators": (',', ': '),
  "cls": ObjectEncoder
}

def dump_graph(nx_graph, dump_path):
  data = json_graph.node_link_data(nx_graph)

  with open(dump_path, "w") as f:
    json.dump(data, f, **DEFAULT_JSON_ARGS)

def load_graph(load_path):
  with open(load_path, "r") as f:
    data = json.load(f)
    nx_graph = json_graph.node_link_graph(data)
    return nx_graph

def dump_results(results, filepath):
  # TODO: might need to write these in pickle
  with open(filepath, "w") as f:
    json.dump(results, f, sort_keys=True, **DEFAULT_JSON_ARGS)
