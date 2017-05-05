set Contents;
set Buckets;

param totalPercentage {c in Contents};
param bucketSpace {b in Buckets};

param M;
param bucketsAllowed;

var amountPlaced {Buckets, Contents} >=0 ;
var forceBucket {Buckets, Contents} binary;


minimize Unallocated_Contents:
    sum{b in Buckets}(bucketSpace[b] - sum{c in Contents}amountPlaced[b,c]);

subject to bucket_capacity {b in Buckets}:
    sum{c in Contents}amountPlaced[b,c] <= bucketSpace[b];

subject to content_Bounds {c in Contents}:
    sum{b in Buckets}amountPlaced[b,c] <= totalPercentage[c];

subject to limit_buckets{c in Contents}:
    sum{b in Buckets}forceBucket[b,c] <= bucketsAllowed;

subject to on_off_switch{b in Buckets, c in Contents}:
    amountPlaced[b,c] <= M * forceBucket[b,c];
