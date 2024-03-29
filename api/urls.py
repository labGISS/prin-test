from django.urls import re_path
from .views import GetSll, GraphBuild, Test, ClusterTest, CompleteQuery, GetExporting, GetClusters, Query3D, SLLMapData

app_name = 'api'
urlpatterns = [
    re_path(r'^slls[/]?$', GetSll.as_view(), name='get_sll_data'),
    re_path(r'^exportings[/]?$', GetExporting.as_view(), name='get_exportings'),
    re_path(r'^graph[/]?$', GraphBuild.as_view(), name='get_graph'),
    re_path(r'^test[/]?$', Test.as_view(), name='test_api'),
    re_path(r'^cluster[/]?$', ClusterTest.as_view(), name='cluster_test'),
    re_path(r'^clusters[/]?$', GetClusters.as_view(), name='get_clusters'),
    re_path(r'^complete[/]?$', CompleteQuery.as_view(), name='complete_query'),
    re_path(r'^graph3d[/]?$', Query3D.as_view(), name='3d_query'),
    re_path(r'^sll-map[/]?$', SLLMapData.as_view(), name='sll_map_data'),
]
