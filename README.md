# sort_assets.py
Input: a file with asset info

Model# Created Assignee

A1208 10/11/2019 Tom

A1209 10/9/2019	John

A1209 10/10/2019 Cat

A1210 10/11/2019 Kim

A1210 10/11/2019 Jim

A1208 10/8/2019	Tim

A1210 10/9/2019	Cam

A1209 10/8/2019	Ken

A1209 10/9/2019	Jack

A1208 10/9/2019	Mary
 
Output: sort the items by Model# and Created date, after that, add a new first column with distinct asset number started at 000001

Asset# Model# Created Assignee

000001 A1208 10/8/2019 Tim

000002 A1208 10/9/2019 Mary

000003 A1208 10/11/2019	Tom

000004 A1209 10/8/2019 Ken

000005 A1209 10/9/2019 John

000006 A1209 10/9/2019 Jack

000007 A1209 10/10/2019	Cat

000008 A1210 10/9/2019	Cam

000009 A1210 10/11/2019	Kim

000010 A1210 10/11/2019	Jim
