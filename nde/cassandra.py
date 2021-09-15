from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
        'secure_connect_bundle': 'G:\internship_project\neuro_data_engg\secure-connect-neurodataengg.zip'
}
auth_provider = PlainTextAuthProvider('MKADFACcMzxpSTFyqqOhRPus', 'wUyqmuv.nnv5kzJZgffSnUymvGSQfiIfoWZZP5zCjcZro-BDgfE_M.ocJ9dKk9pken26fCJgG9bp.8PpMnPab_eUDiAOST1MkdK9kLGL,0K6OgC+Q5wIHBNEyu1ZTyPs')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")
####################################################################################

# from cassandra.cluster import Cluster
# from cassandra.auth import PlainTextAuthProvider

# cloud_config= {
#         'secure_connect_bundle': 'G:\internship_project\neuro_data_engg\secure-connect-sd.zip'
# }
# auth_provider = PlainTextAuthProvider('enlinqESSEkETcfRtkxHRMZA', '_wF,ANc-JWPjZmIIS6dEWKT38WXGmxx55.v5s.7BQB0LKfdSw4_IZ3WArpb8uQsbbOY9JS2CbpOrcInaO7uofac9nRzKb.b6+ll5z70iiSbyd9xe_XxhGFaM+El8-PIM')
# cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
# session = cluster.connect()

# row = session.execute("select release_version from system.local").one()
# if row:
#     print(row[0])
# else:
#     print("An error occurred.")