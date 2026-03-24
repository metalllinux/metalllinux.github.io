---
title: "Good Command To Check The Irq Balance Of Cpu Cores From An Sosreport"
category: "rocky-linux"
tags: ["rocky-linux", "good", "command", "check", "irq"]
---

[vncuser@myx86 sosreport-c003psrwk10705-2025-09-02-ttfiozx]$ awk -F': ' '/rx_queue_[0-9]+_packets:/ {                                                                                                                                                                 q=$1; sub("rx_queue_","",q); sub("_packets","",q);
    print q, $2
}' "$f" | sort -k2,2nr | head -10 > top_queues.txt
[vncuser@myx86 sosreport-c003psrwk10705-2025-09-02-ttfiozx]$ while read q pkts; do     irq=$(grep "ice-em3-TxRx-$q" proc/interrupts | awk '{print $1}' | tr -d :);     cpu=$(cat proc/irq/$irq/smp_affinity_list 2>/dev/null);     printf "queue=%-3s pkts=%s irq=%s cpu_affinity=%s\n" "$q" "$pkts" "$irq" "$cpu"; done < top_queues.txt
queue=50  pkts=36038863894 irq=980 cpu_affinity=70
queue=116 pkts=17193196220 irq=1046 cpu_affinity=64
queue=40  pkts=15633604912 irq=970 cpu_affinity=66
queue=0   pkts=15044858429 irq=930 cpu_affinity=68
queue=15  pkts=14155283183 irq=945 cpu_affinity=64
queue=92  pkts=13001241510 irq=1022 cpu_affinity=2
queue=93  pkts=12939168509 irq=1023 cpu_affinity=64
queue=35  pkts=12550676148 irq=965 cpu_affinity=64
queue=31  pkts=11137117687 irq=961 cpu_affinity=64

