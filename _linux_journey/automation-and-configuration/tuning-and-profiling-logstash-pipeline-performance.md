---
title: "Tuning And Profiling Logstash Pipeline Performance"
category: "automation-and-configuration"
tags: ["automation-and-configuration", "tuning", "profiling", "logstash", "pipeline"]
---

New

The executive guide to generative AI

[Read more](https://www.elastic.co/portfolio/operationalising-generative-ai-strategic-guide)

[About us](https://www.elastic.co/about)[Partners](https://www.elastic.co/partners)[Support](https://www.elastic.co/support)|[Login](https://cloud.elastic.co/login)

[](https://www.elastic.co/)

[Pricing](https://www.elastic.co/pricing)[Docs](https://www.elastic.co/docs)

- Logstash Reference:
- [Logstash Introduction](https://www.elastic.co/guide/en/logstash/current/introduction.html)
- [Getting Started with Logstash](https://www.elastic.co/guide/en/logstash/current/getting-started-with-logstash.html)
- [How Logstash Works](https://www.elastic.co/guide/en/logstash/current/pipeline.html)
- [Setting Up and Running Logstash](https://www.elastic.co/guide/en/logstash/current/setup-logstash.html)
- [Upgrading Logstash](https://www.elastic.co/guide/en/logstash/current/upgrading-logstash.html)
- [Creating a Logstash pipeline](https://www.elastic.co/guide/en/logstash/current/configuration.html)
- [Secure your connection](https://www.elastic.co/guide/en/logstash/current/ls-security.html)
- [Advanced Logstash Configurations](https://www.elastic.co/guide/en/logstash/current/configuration-advanced.html)
- [Logstash-to-Logstash communication](https://www.elastic.co/guide/en/logstash/current/ls-to-ls.html)
- [Managing Logstash](https://www.elastic.co/guide/en/logstash/current/config-management.html)
- [Using Logstash with Elastic Integrations](https://www.elastic.co/guide/en/logstash/current/ea-integrations.html)
- [Working with Logstash Modules](https://www.elastic.co/guide/en/logstash/current/logstash-modules.html)
- [Working with Filebeat Modules](https://www.elastic.co/guide/en/logstash/current/filebeat-modules.html)
- [Working with Winlogbeat Modules](https://www.elastic.co/guide/en/logstash/current/winlogbeat-modules.html)
- [Queues and data resiliency](https://www.elastic.co/guide/en/logstash/current/resiliency.html)
- [Transforming Data](https://www.elastic.co/guide/en/logstash/current/transformation.html)
- [Deploying and Scaling Logstash](https://www.elastic.co/guide/en/logstash/current/deploying-and-scaling.html)
- [Managing GeoIP Databases](https://www.elastic.co/guide/en/logstash/current/geoip-database-management.html)
- [Performance tuning](https://www.elastic.co/guide/en/logstash/current/performance-tuning.html)
    - [Performance troubleshooting](https://www.elastic.co/guide/en/logstash/current/performance-troubleshooting.html)
    - [Tuning and profiling logstash pipeline performance](https://www.elastic.co/guide/en/logstash/current/tuning-logstash.html)
- [Monitoring Logstash with Elastic Agent](https://www.elastic.co/guide/en/logstash/current/monitoring-with-ea.html)
- [Monitoring Logstash (legacy)](https://www.elastic.co/guide/en/logstash/current/configuring-logstash.html)
- [Monitoring Logstash with APIs](https://www.elastic.co/guide/en/logstash/current/monitoring-logstash.html)
- [Working with plugins](https://www.elastic.co/guide/en/logstash/current/working-with-plugins.html)
- [Integration plugins](https://www.elastic.co/guide/en/logstash/current/plugin-integrations.html)
- [Input plugins](https://www.elastic.co/guide/en/logstash/current/input-plugins.html)
- [Output plugins](https://www.elastic.co/guide/en/logstash/current/output-plugins.html)
- [Filter plugins](https://www.elastic.co/guide/en/logstash/current/filter-plugins.html)
- [Codec plugins](https://www.elastic.co/guide/en/logstash/current/codec-plugins.html)
- [Tips and best practices](https://www.elastic.co/guide/en/logstash/current/tips.html)
- [Troubleshooting](https://www.elastic.co/guide/en/logstash/current/troubleshooting.html)
- [Contributing to Logstash](https://www.elastic.co/guide/en/logstash/current/contributing-to-logstash.html)
- [Contributing a Java Plugin](https://www.elastic.co/guide/en/logstash/current/contributing-java-plugin.html)
- [Breaking changes](https://www.elastic.co/guide/en/logstash/current/breaking-changes.html)
- [Release Notes](https://www.elastic.co/guide/en/logstash/current/releasenotes.html)

[Elastic Docs](https://www.elastic.co/guide/) ›[Logstash Reference \[8.17\]](https://www.elastic.co/guide/en/logstash/current/index.html) ›[Performance tuning](https://www.elastic.co/guide/en/logstash/current/performance-tuning.html)

# <a id="id-1"></a>Tuning and profiling logstash pipeline performance

[edit](https://github.com/elastic/logstash/edit/8.17/docs/static/performance-checklist.asciidoc "Edit this page on GitHub")

The [Flow Metrics](https://www.elastic.co/guide/en/logstash/current/node-stats-api.html#flow-stats "Flow stats") in Logstash’s Monitoring API can provide excellent insight into how events are flowing through your pipelines. They can reveal whether your pipeline is constrained for resources, which parts of your pipeline are consuming the most resources, and provide useful feedback when tuning.

## <a id="tuning-logstash-worker-utilisation"></a>[](#tuning-logstash-worker-utilisation)Worker utilisation

[edit](https://github.com/elastic/logstash/edit/8.17/docs/static/performance-checklist.asciidoc "Edit this page on GitHub")

When a pipeline’s `worker_utilization` flow metric is consistently near 100, all of its workers are occupied processing the filters and outputs of the pipeline. We can see *which* plugins in the pipeline are consuming the available worker capacity by looking at the plugin-level `worker_utilization` and `worker_millis_per_event` flow metrics. Using this information, we can gain intuition about how to tune the pipeline’s settings to add resources, how to find and eliminate wasteful computation, or realise the need to scale up/out the capacity of downstream destinations.

In general, plugins fit into one of two categories:

- **CPU-bound**: plugins that perform computation on the contents of events *without* the use of the network or disk IO tend to benefit from incrementally increasing `pipeline.workers` as long as the process has available CPU; once CPU is exhausted additional concurrency can result in *lower* throughput as the pipeline workers contend for resources and the amount of time spent in context-switching increases.
- **IO-bound**: plugins that use the network to either enrich events or transmit events tend to benefit from incrementally increasing `pipeline.workers` and/or tuning the `pipeline.batch.*` parameters described below. This allows them to make better use of network resources, as long as those external services are not exerting back-pressure (even if Logstash is using nearly all of its available CPU).

The further a pipeline’s `worker_utilization` is from 100, the more time its workers are spending waiting for events to arrive in the queue. Because the volume of data in most pipelines is often inconsistent, the goal should be to tune the pipeline such that it has the resources to avoid propagating back-pressure to its inputs during peak periods.

## <a id="tuning-logstash-queue-backpressure"></a>[](#tuning-logstash-queue-backpressure)Queue back-pressure

[edit](https://github.com/elastic/logstash/edit/8.17/docs/static/performance-checklist.asciidoc "Edit this page on GitHub")

When a pipeline receives events faster than it can process them, the inputs eventually experience back-pressure that prevents them from receiving additional events. Depending on the input plugin being used, back-pressure can either propagate upstream or lead to data loss.

A pipeline’s `queue_backpressure` flow metric reflects how much time the inputs are spending attempting to push events into the queue. The metric isn’t precisely comparable across pipelines, but instead allows you to compare a single pipeline’s current behaviour to *itself* over time. When this metric is growing, look *downstream* at the pipeline’s filters and outputs to see if they are using resources effectively, have sufficient resources allocated, or are experiencing back-pressure of their own.

A persisted queue offers durability guarantees and can absorb back-pressure for longer than the default in-memory queue, but once it is full it too propagates back-pressure. The `queue_persisted_growth_events` flow metric is useful measure of how much back-pressure is being actively absorbed by the persisted queue, and should trend toward zero (or less) over the pipeline’s lifetime. Negative numbers indicate that the queue is *shrinking*, and that the workers are catching up on lag that had previously developed.

## <a id="tuning-logstash-settings"></a>[](#tuning-logstash-settings)Tuning-related settings

[edit](https://github.com/elastic/logstash/edit/8.17/docs/static/performance-checklist.asciidoc "Edit this page on GitHub")

The Logstash defaults are chosen to provide fast, safe performance for most users. However if you notice performance issues, you may need to modify some of the defaults. Logstash provides the following configurable options for tuning pipeline performance: `pipeline.workers`, `pipeline.batch.size`, and `pipeline.batch.delay`.

For more information about setting these options, see [logstash.yml](https://www.elastic.co/guide/en/logstash/current/logstash-settings-file.html "logstash.yml").

Make sure you’ve read the [Performance troubleshooting](https://www.elastic.co/guide/en/logstash/current/performance-troubleshooting.html "Performance troubleshooting") before modifying these options.

- The `pipeline.workers` setting determines how many threads to run for filter and output processing. If you find that events are backing up, or that the CPU is not saturated, consider increasing the value of this parameter to make better use of available processing power. Good results can even be found increasing this number past the number of available processors as these threads may spend significant time in an I/O wait state when writing to external systems.
- The `pipeline.batch.size` setting defines the maximum number of events an individual worker thread collects from the queue before attempting to execute filters and outputs. Larger batch sizes are generally more efficient, but increase memory overhead. Output plugins can process each batch as a logical unit. The Elasticsearch output, for example, attempts to send a single [bulk request](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html) for each batch received. Tuning the `pipeline.batch.size` setting adjusts the size of bulk requests sent to Elasticsearch.
- The `pipeline.batch.delay` setting rarely needs to be tuned. This setting adjusts the latency of the Logstash pipeline. Pipeline batch delay is the maximum amount of time in milliseconds that a pipeline worker waits for each new event while its current batch is not yet full. After this time elapses without any more events becoming available, the worker begins to execute filters and outputs. The maximum time that the worker waits between receiving an event and processing that event in a filter is the product of the `pipeline.batch.delay` and `pipeline.batch.size` settings.

## <a id="_notes_on_pipeline_configuration_and_performance"></a>[](#_notes_on_pipeline_configuration_and_performance)Notes on pipeline configuration and performance

[edit](https://github.com/elastic/logstash/edit/8.17/docs/static/performance-checklist.asciidoc "Edit this page on GitHub")

If you plan to modify the default pipeline settings, take into account the following suggestions:

- The total number of inflight events is determined by the product of the `pipeline.workers` and `pipeline.batch.size` settings. This product is referred to as the *inflight count*. Keep the value of the inflight count in mind as you adjust the `pipeline.workers` and `pipeline.batch.size` settings. Pipelines that intermittently receive large events at irregular intervals require sufficient memory to handle these spikes. Set the JVM heap space accordingly in the `jvm.options` config file (See [Logstash Configuration Files](https://www.elastic.co/guide/en/logstash/current/config-setting-files.html "Logstash Configuration Files") for more info).
- Measure each change to make sure it increases, rather than decreases, performance.
- Ensure that you leave enough memory available to cope with a sudden increase in event size. For example, an application that generates exceptions that are represented as large blobs of text.
- The number of workers may be set higher than the number of CPU cores since outputs often spend idle time in I/O wait conditions.
- Threads in Java have names and you can use the `jstack`, `top`, and the VisualVM graphical tools to figure out which resources a given thread uses.
- On Linux platforms, Logstash labels its threads with descriptive names. For example, inputs show up as `[base]<inputname`, and pipeline workers show up as `[base]>workerN`, where N is an integer. Where possible, other threads are also labeled to help you identify their purpose.

## <a id="profiling-the-heap"></a>[](#profiling-the-heap)Profiling the heap

[edit](https://github.com/elastic/logstash/edit/8.17/docs/static/performance-checklist.asciidoc "Edit this page on GitHub")

When tuning Logstash you may have to adjust the heap size. You can use the [VisualVM](https://visualvm.github.io/) tool to profile the heap. The **Monitor** pane in particular is useful for checking whether your heap allocation is sufficient for the current workload. The screenshots below show sample **Monitor** panes. The first pane examines a Logstash instance configured with too many inflight events. The second pane examines a Logstash instance configured with an appropriate amount of inflight events. Note that the specific batch sizes used here are most likely not applicable to your specific workload, as the memory demands of Logstash vary in large part based on the type of messages you are sending.

![pipeline overload](../_resources/pipeline_overload_f07474b5d43d4fe385fb47ec0662394e.png)

![pipeline correct load](../_resources/pipeline_correct_load_84812638f8054023b239256afb7e.png)

In the first example we see that the CPU isn’t being used very efficiently. In fact, the JVM is often times having to stop the VM for “full GCs”. Full garbage collections are a common symptom of excessive memory pressure. This is visible in the spiky pattern on the CPU chart. In the more efficiently configured example, the GC graph pattern is more smooth, and the CPU is used in a more uniform manner. You can also see that there is ample headroom between the allocated heap size, and the maximum allowed, giving the JVM GC a lot of room to work with.

Examining the in-depth GC statistics with a tool similar to the excellent [VisualGC](https://visualvm.github.io/plugins.html) plugin shows that the over-allocated VM spends very little time in the efficient Eden GC, compared to the time spent in the more resource-intensive Old Gen “Full” GCs.

As long as the GC pattern is acceptable, heap sizes that occasionally increase to the maximum are acceptable. Such heap size spikes happen in response to a burst of large events passing through the pipeline. In general practice, maintain a gap between the used amount of heap memory and the maximum. This document is not a comprehensive guide to JVM GC tuning. Read the official [Oracle guide](http://www.oracle.com/webfolder/technetwork/tutorials/obe/java/gc01/index.html) for more information on the topic. We also recommend reading [Debugging Java Performance](https://www.semicomplete.com/blog/geekery/debugging-java-performance/).

[« Performance troubleshooting](https://www.elastic.co/guide/en/logstash/current/performance-troubleshooting.html) [Monitoring Logstash with Elastic Agent »](https://www.elastic.co/guide/en/logstash/current/monitoring-with-ea.html)

On this page

- [Worker utilisation](#tuning-logstash-worker-utilisation)
- [Queue back-pressure](#tuning-logstash-queue-backpressure)
- [Tuning-related settings](#tuning-logstash-settings)
- [Notes on pipeline configuration and performance](#_notes_on_pipeline_configuration_and_performance)
- [Profiling the heap](#profiling-the-heap)

Most Popular

Video

[Get Started with Elasticsearch](https://www.elastic.co/webinars/getting-started-elasticsearch?page=docs&placement=top-video)

Video

[Intro to Kibana](https://www.elastic.co/webinars/getting-started-kibana?page=docs&placement=top-video)

Video

[ELK for Logs & Metrics](https://www.elastic.co/webinars/introduction-elk-stack?page=docs&placement=top-video)

Was this helpful?

Feedback

<img width="192" height="67" src="../_resources/logo-tagline_secondary_all_white_6bf42be063a04355a.svg"/>](https://www.elastic.co/)

## Follow us

- <a id="footer_linkedin"></a>[![Elastic's LinkedIn page](../_resources/footer-icon-linkedin_6a057cd7996d41389440471a4c9db.svg)](https://www.linkedin.com/company/elastic-co)
- <a id="footer_youtube"></a>[![Elastic's YouTube page](../_resources/footer-icon-youtube_9d92864f3d3e40d092184fa3116f24.svg)](https://www.youtube.com/user/elasticsearch)
- <a id="footer_facebook"></a>[![Elastic's Facebook page](../_resources/footer-icon-facebook_d801ab9fd927492c8a75a9051d49b.svg)](https://www.facebook.com/elastic.co)
- <a id="footer_twitter"></a>[![Elastic's Twitter page](../_resources/footer-icon-twitter_ec9e22beb4514c0c8b20d0ee0ab8b1.svg)](https://www.twitter.com/elastic)
- [![Elastic's GitHub page](../_resources/icon-footer-github_27adafd9d1ea441a8fa733356c80f28.svg)](https://github.com/elastic)

- ## About us
    
    [About Elastic](https://www.elastic.co/about/)[Leadership](https://www.elastic.co/about/leadership)[Blog](https://www.elastic.co/blog)[Newsroom](https://www.elastic.co/about/press)
    
- ## Join us
    
    [Careers](https://www.elastic.co/careers)[Career portal](https://jobs.elastic.co/#/)[How we hire](https://www.elastic.co/careers/how-we-hire)
    

- ## Partners
    
    [Find a partner](https://partners.elastic.co/findapartner/)[Partner login](https://cloud.elastic.co/login?redirectTo=https://partners.elastic.co/English/Partner/home.aspx)[Request access](https://partners.elastic.co/English/register_email.aspx)[Become a partner](https://www.elastic.co/partners/become-a-partner)
    
- ## Trust & Security
    
    [Trust centre](https://www.elastic.co/trust)[EthicsPoint portal](https://secure.ethicspoint.com/domain/media/en/gui/74447/index.html)[ECCN report](https://www.elastic.co/trust/business-integrity#international-trade-compliance—eccn-information)[Ethics email](mailto:ethics@elastic.co)
    

- ## Investor relations
    
    [Investor resources](https://ir.elastic.co/home/default.aspx)[Governance](https://ir.elastic.co/governance/corporate-governance/default.aspx)[Financials](https://ir.elastic.co/financials/quarterly-results/default.aspx)[Stock](https://ir.elastic.co/stock/stock-quote/default.aspx)
    
- ## Excellence Awards
    
    [Previous winners](https://www.elastic.co/blog/2022-elastic-excellence-awards-winners)[ElasticON Tour](https://www.elastic.co/elasticon)[Become a sponsor](https://www.elastic.co/events/sponsor)[All events](https://www.elastic.co/events/)
    

- [Trademarks](https://www.elastic.co/legal/trademarks)
- [Terms of Use](https://www.elastic.co/legal/terms-of-use)
- [Privacy](https://www.elastic.co/legal/privacy-statement)
- [Sitemap](https://www.elastic.co/sitemap)

© 2025. Elasticsearch B.V. All Rights Reserved

Elastic, Elasticsearch and other related marks are trademarks, logos or registered trademarks of Elasticsearch B.V. in the United States and other countries.

Apache, Apache Lucene, Apache Hadoop, Hadoop, HDFS and the yellow elephant logo are trademarks of the [Apache Software Foundation](https://www.apache.org/) in the United States and/or other countries. All other brand names, product names, or trademarks belong to their respective owners.