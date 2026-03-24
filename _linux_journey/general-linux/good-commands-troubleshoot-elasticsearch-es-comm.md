---
title: "Steps to Troubleshoot - Cluster Red"
category: "general-linux"
tags: ["good", "commands", "troubleshoot", "elasticsearch", "comm"]
---

### Steps to Troubleshoot - Cluster Red

Cluster Health

`curl -ks "https://localhost:9200/_cluster/health?pretty"`

OR

`curl -k -XGET "https://localhost:9200/_cluster/health?pretty"`

Cluster Settings

`curl -ks "https://localhost:9200/_cluster/settings?pretty"`

Unassigned Shards with reason

`curl -ks -XGET https://localhost:9200/_cat/shards?h=index,shard,prirep,state,unassigned.reason | grep UNASSIGNED`

Allocation Explanation

1.  `curl -ks 'https://localhost:9200/_cluster/allocation/explain?pretty'`
    
2.  Recovering Shards Progress
    

`curl -ks -XGET "https://localhost:9200/_cat/recovery?v&h=index,shard,time,source_node,target_node,files_percent,bytes_percent&detailed=true&active_only=true"`

6\. Indice setting

`curl -k -XGET 'https://localhost:9200/&lt;index_name>/_settings?pretty'`

7\. Command to check which ES service(s) auto-restarted recently

`ansible all -i /opt/exabeam_installer/inventory -m shell -ba 'for i in $(ls -1 /etc/systemd/system/ | grep elasticsearch-[abcdefghijkl] |cut -d\. -f 1); do sudo systemctl status $i | grep -B 3 Active |grep -v loaded| tr -d \\\n ; echo "" ; done'`

`8. Check Shard Recovery Progress`

`curl -ks -XGET "https://localhost:9200/_cat/recovery?detailed=true&active_only=true&h=index,shard,time,source_node,target_node,bytes,bytes_percent" | sort -k4,5 -V`

11. Current Retention Settings:
curl -ks https://localhost:9200/_cat/indices |sort -k3

12. How to Check Indicies
curl -k https://localhost:9200/_cat/indices?v

Check if indicies are in read-only mode:

13. curl -ks https://localhost:9200/<INDEX>*/_settings?pretty | grep read_only_allow_delete

Set any indices in read-only mode to false.

14. curl -ks -XPUT -H "Content-Type: application/json" https://localhost:9200/_all/_settings -d '{"index.blocks.read_only_allow_delete": false}'

16. How Check Which ES Hosts are Assigned to Which Hosts.

curl -k "https://localhost:9200/_cat/nodeattrs?v" | sort

17. Manually send shards between warm nodes.

curl -ks -XPOST https://localhost:9200/_cluster/reroute?pretty -H 'Content-Type: application/json' -d '{"commands":[{"move":{"index":"<NAME>-2023.02.22", "shard":0,"from_node":"host1-2","to_node":"host2-1"}}]}'

19. Exclude a particular host:

1 or 2 Node DL

For small DL cluster with 1 or 2 nodes, Shard of one index can’t be moved to one node because of elasticsaerch’s . The formal explanation is like:

    "there are too many copies of the shard allocated to nodes with attribute [rack_id], there are [2] total configured shard copies for this shard id and [2] total attribute values, expected the allocated shard count per attribute [2] to be less than or equal to the upper bound of the required number of shards per attribute [1]"

So when this case happens, firstly we need to exclude the hot node in case that new data comes in
curl -ks -XPUT "https://127.0.0.1:9200/_cluster/settings?pretty" -H 'Content-Type: application/json' -d'{
  "transient" : {
    "cluster.routing.allocation.exclude._name" : "host1-1"
  }
}'

Then we will move indices on hot nodes to warm node, by running:
curl -ks "https://localhost:9200/<index_name>/_settings" -d '{"index":{"routing.allocation.require.box_type":"warm"}}' -XPUT -H 'Content-Type: application/json'

After action on hot nodes, we can move indices back to hot nodes by running:
curl -ks "https://localhost:9200/<index_name>/_settings" -d '{"index":{"routing.allocation.require.box_type":"hot"}}' -XPUT -H 'Content-Type: application/json'

curl -kX POST "https://localhost:9200/_cluster/reroute?pretty"

Finally, you can run command to check the cluster health’s number_of_pending_tasks, unassigned_shards and initializing_shards fields to monitor the recovery process:
watch curl -k https://localhost:9200/_cluster/health?pretty

If Indices are stuck and not progressing, please run:

curl -ks -XPUT -H "Content-Type: application/json" https://localhost:9200/_all/_settings -d '{"index.blocks.read_only_allow_delete": false}'

