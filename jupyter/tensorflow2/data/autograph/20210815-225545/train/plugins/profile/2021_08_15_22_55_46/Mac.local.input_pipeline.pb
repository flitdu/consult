	sh??|oY@sh??|oY@!sh??|oY@	????+??????+??!????+??"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$sh??|oY@?l??????A??C?lgY@Y9??v????*	    P??@2o
8Iterator::Model::Prefetch::BatchV2::Shuffle::ParallelMap]fffff?R@!^p?A ?X@)fffff?R@1^p?A ?X@:Preprocessing2b
+Iterator::Model::Prefetch::BatchV2::ShuffledB`??"?R@!&?5h??X@)??|?5^??1R??+?o??:Preprocessing2x
AIterator::Model::Prefetch::BatchV2::Shuffle::ParallelMap::Shufflec?K7?A`??!6??a!??)?K7?A`??16??a!??:Preprocessing2F
Iterator::ModelZd;?O???!??#t???)y?&1???1?( ުݒ?:Preprocessing2P
Iterator::Model::Prefetch;?O??n??!c?M??A??);?O??n??1c?M??A??:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
device?Your program is NOT input-bound because only 0.1% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*no#You may skip the rest of this page.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	?l???????l??????!?l??????      ??!       "      ??!       *      ??!       2	??C?lgY@??C?lgY@!??C?lgY@:      ??!       B      ??!       J	9??v????9??v????!9??v????R      ??!       Z	9??v????9??v????!9??v????JCPU_ONLY