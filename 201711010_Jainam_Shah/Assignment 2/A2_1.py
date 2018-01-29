#201711010- JAINAM SHAH

from elasticsearch import Elasticsearch
es = Elasticsearch()

#1.boolean queries

# printing entries with sub-genre:history,author:Steinbeck, John and number of pages 175 or 323
res = es.search(index = 'book-5', body={
            "query": {
                        "bool" : {
                          "must" : {
                            "match" : { "sub-genere" : "history" }
                          },
                          "filter": {
                            "match" : { "author" : "Steinbeck, John" }
                          },
                          "should" : [
                            { "match" : { "pages" : 323 } },
                            { "match" : { "pages" : 175 } }
                          ],
                           "minimum_should_match" : 0,
                        }
                      }
                    })
print(" response1: {}".format(res))
#printing entries with author Steinbeck, John
print('='*200)
res = es.search(index = 'book-5', body={
            "query": {
                        "bool" : {
                          "must" : {
                            "match" : { "author" : "Steinbeck, John" }
                          }
                          }
                      }
                      })
print(" response2: {}".format(res))

#printing entries with sub-genre:novel
print('='*200)
res = es.search(index = 'book-5', body={
            "query": {
                        "bool" : {
                          "must" : {
                            "match" : { "sub-genere" : "novel" }
                          }
                          }
                      }
                      })
print(" response3: {}".format(res))

#2.boosting queries

print('='*200)

res = es.search(index = 'book-5', body={
            "query": {
                        "boosting" : {
                                    "positive" : {
                                        "term" : {
                                            #"pages" : "112"
                                            "genere" : "fiction"
                                        }
                                    },
                                    "negative" : {
                                         "term" : {
                                             "pages" : "177"
                                             #"genere" : "abcd"
                                        }
                                    },
                                    "negative_boost" : 0.8
                                }

                      }
                    })
print(" response4: {}".format(res))

print('='*200)

#genre changed to tech
res = es.search(index = 'book-5', body={
            "query": {
                        "boosting" : {
                                    "positive" : {
                                        "term" : {
                                            #"pages" : "112"
                                            "genere" : "tech"
                                        }
                                    },
                                    "negative" : {
                                         "term" : {
                                             "pages" : "177"
                                             #"genere" : "abcd"
                                        }
                                    },
                                    "negative_boost" : 0.8
                                }

                      }
                    })
print(" response5: {}".format(res))

print('='*200)

#number of pages changed to 150
res = es.search(index = 'book-5', body={
            "query": {
                        "boosting" : {
                                    "positive" : {
                                        "term" : {
                                            #"pages" : "112"
                                            "genere" : "fiction"
                                        }
                                    },
                                    "negative" : {
                                         "term" : {
                                             "pages" : "150"
                                             #"genere" : "abcd"
                                        }
                                    },
                                    "negative_boost" : 0.8
                                }

                      }
                    })
print(" response6: {}".format(res))

print('='*200)

#3.minimum_should_match

res = es.search(index = 'book-5', body={
 "query": {
    "bool" : {
      "must" : {
        "match" : { "publisher" : "O'Reilly" }
      },
      "filter": {
        "match" : { "sub-genere" : "data_science" }
      },
      "should" : [
        { "match" : { "genere" : "fiction" } },
        { "match" : { "genere" : "tech" } }
      ],
       "minimum_should_match" : 1,
    }
    }
   })
print(" response7: {}".format(res))

print('='*200)
#above with one genre changed to data-science
res = es.search(index = 'book-5', body={
 "query": {
    "bool" : {
      "must" : {
        "match" : { "publisher" : "O'Reilly" }
      },
      "should" : [
        { "match" : { "genere" : "tech" } },
        { "match" : { "sub-genere" : "data-science" } }
      ],
       "minimum_should_match" : 2,
    }
    }
   })
print(" response8: {}".format(res))

#above with minimum_should_match = 1
print('='*200)

res = es.search(index = 'book-5', body={
 "query": {
    "bool" : {
      "must" : {
        "match" : { "publisher" : "O'Reilly" }
      },
      "should" : [
        { "match" : { "genere" : "tech" } },
        { "match" : { "sub-genere" : "data-science" } }
      ],
       "minimum_should_match" : 1,
    }
    }
   })
print(" response9: {}".format(res))

#publisher changed to Prentice hall


print('='*200)

res = es.search(index = 'book-5', body={
 "query": {
    "bool" : {
      "must" : {
        "match" : { "publisher" : "Prentice Hall" }
      },
      "should" : [
        { "match" : { "genere" : "tech" } },
        { "match" : { "sub-genere" : "data-science" } }
      ],
       "minimum_should_match" : 2,
    }
    }
   })
print(" response10: {}".format(res))

print('='*200)
#above with minimum_should_match = 1
res = es.search(index = 'book-5', body={
 "query": {
    "bool" : {
      "must" : {
        "match" : { "publisher" : "Prentice Hall" }
      },
      "should" : [
        { "match" : { "genere" : "tech" } },
        { "match" : { "sub-genere" : "data-science" } }
      ],
       "minimum_should_match" : 1,
    }
    }
   })
print(" response11: {}".format(res))

print('='*200)
#above with minimum_should_match = 0
res = es.search(index = 'book-5', body={
 "query": {
    "bool" : {
      "must" : {
        "match" : { "publisher" : "Prentice Hall" }
      },
      "should" : [
        { "match" : { "genere" : "tech" } },
        { "match" : { "sub-genere" : "data-science" } }
      ],
       "minimum_should_match" : 0,
    }
    }
   })
print(" response12: {}".format(res))



#output of file
"""E:\Vandan\DA-IICT\Academic Docs\Sem 2\IT562\Assignment 2>python A2_1.py
 response1: {'took': 1, 'timed_out': False, '_shards': {'total': 5, 'successful': 5, 'skipped': 0, 'failed': 0}, 'hits': {'total': 2, 'max_score': 2.0329216, 'hits': [{'_index': 'book-5', '_type': 'book-map', '_id': 'dlm1CGEBztpV5x6Npn2P', '_score': 2.0329216, '_source': {'title': 'Russian Journal, A', 'author': 'Steinbeck, John', 'genere': 'nonfiction', 'sub-genere': 'history', 'pages': '196', 'publisher': 'Penguin'}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'fVm1CGEBztpV5x6NqX1H', '_score': 1.5234954, '_source': {'title': 'Once There Was a War', 'author': 'Steinbeck, John', 'genere': 'nonfiction', 'sub-genere': 'history', 'pages': '196', 'publisher': 'Penguin'}}]}}
========================================================================================================================================================================================================
 response2: {'took': 1, 'timed_out': False, '_shards': {'total': 5, 'successful': 5, 'skipped': 0, 'failed': 0}, 'hits': {'total': 11, 'max_score': 6.0498424, 'hits': [{'_index': 'book-5', '_type': 'book-map', '_id': 'fVm1CGEBztpV5x6NqX1H', '_score': 6.0498424, '_source': {'title': 'Once There Was a War', 'author': 'Steinbeck, John', 'genere': 'nonfiction', 'sub-genere': 'history', 'pages': '196', 'publisher': 'Penguin'}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'flm1CGEBztpV5x6NqX2s', '_score': 5.823662, '_source': {'title': 'Moon is Down, The', 'author': 'Steinbeck, John', 'genere': 'fiction', 'sub-genere': 'classic', 'pages': '196', 'publisher': 'Penguin'}}, {'_index': 'book-5', '_type': 'book-map', '_id': '5Fm1CGEBztpV5x6N0H39', '_score': 5.823662, '_source': {'title': 'Life in Letters, A', 'author': 'Steinbeck, John', 'genere': 'nonfiction', 'sub-genere': 'autobiography', 'pages': '196', 'publisher': ''}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'fFm1CGEBztpV5x6NqH3z', '_score': 4.903469, '_source': {'title': 'Journal of a Novel', 'author': 'Steinbeck, John', 'genere': 'fiction', 'sub-genere': 'classic', 'pages': '196', 'publisher': 'Penguin'}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'pVm1CGEBztpV5x6Nt31f', '_score': 4.903469, '_source': {'title': 'Winter of Our Discontent, The', 'author': 'Steinbeck, John', 'genere': 'fiction', 'sub-genere': 'classic', 'pages': '196', 'publisher': 'Penguin'}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'dlm1CGEBztpV5x6Npn2P', '_score': 4.792208, '_source': {'title': 'Russian Journal, A', 'author': 'Steinbeck, John', 'genere': 'nonfiction', 'sub-genere': 'history', 'pages': '196', 'publisher': 'Penguin'}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'rlm1CGEBztpV5x6Nun2a', '_score': 4.792208, '_source': {'title': 'Burning Bright', 'author': 'Steinbeck, John', 'genere': 'fiction', 'sub-genere': 'classic', 'pages': '175', 'publisher': 'Penguin'}}, {'_index': 'book-5', '_type': 'book-map', '_id': '61m1CGEBztpV5x6N031R', '_score': 4.792208, '_source': {'title': 'Grapes of Wrath, The', 'author': 'Steinbeck, John', 'genere': 'fiction', 'sub-genere': 'classic', 'pages': '196', 'publisher': ''}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'Tlm1CGEBztpV5x6Nln1h', '_score': 2.9847333, '_source': {'title': 'Data Smart', 'author': 'Foreman, John', 'genere': 'tech', 'sub-genere': 'data_science', 'pages': '235', 'publisher': 'Wiley'}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'XVm1CGEBztpV5x6NnX0o', '_score': 2.9847333, '_source': {'title': "Statistical Decision Theory'", 'author': 'Pratt, John', 'genere': 'tech', 'sub-genere': 'data_science', 'pages': '236', 'publisher': 'MIT Press'}}]}}
========================================================================================================================================================================================================
 response3: {'took': 1, 'timed_out': False, '_shards': {'total': 5, 'successful': 5, 'skipped': 0, 'failed': 0}, 'hits': {'total': 38, 'max_score': 2.0329216, 'hits': [{'_index': 'book-5', '_type': 'book-map', '_id': 'kFm1CGEBztpV5x6Nr329', '_score': 2.0329216, '_source': {'title': 'Sea of Poppies', 'author': 'Ghosh, Amitav', 'genere': 'fiction', 'sub-genere': 'novel', 'pages': '197', 'publisher': 'Penguin'}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'dVm1CGEBztpV5x6Npn06', '_score': 2.0329216, '_source': {'title': 'Jurassic Park', 'author': 'Crichton, Michael', 'genere': 'fiction', 'sub-genere': 'novel', 'pages': '174', 'publisher': 'Random House'}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'X1m1CGEBztpV5x6NnX3P', '_score': 2.0329216, '_source': {'title': 'New Machiavelli, The', 'author': 'Wells, H. G.', 'genere': 'fiction', 'sub-genere': 'novel', 'pages': '180', 'publisher': 'Penguin'}}, {'_index': 'book-5', '_type': 'book-map', '_id': '9Vm1CGEBztpV5x6N130q', '_score': 2.0329216, '_source': {'title': '20000 Leagues Under the Sea', 'author': 'Verne, Jules', 'genere': 'fiction', 'sub-genere': 'novel', 'pages': '190', 'publisher': ''}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'Dlm1CGEBztpV5x6N4H5p', '_score': 2.0329216, '_source': {'title': 'More Tears to Cry', 'author': 'Sassoon, Jean', 'genere': 'fiction', 'sub-genere': 'novel', 'pages': '235', 'publisher': ''}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'yVm1CGEBztpV5x6Nxn2v', '_score': 2.020018, '_source': {'title': 'Deceiver, The', 'author': 'Forsyth, Frederick', 'genere': 'fiction', 'sub-genere': 'novel', 'pages': '178', 'publisher': ''}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'zFm1CGEBztpV5x6Nx33I', '_score': 2.020018, '_source': {'title': 'Rosy is My Relative', 'author': 'Durrell, Gerald', 'genere': 'fiction', 'sub-genere': 'novel', 'pages': '176', 'publisher': ''}}, {'_index': 'book-5', '_type': 'book-map', '_id': '0Fm1CGEBztpV5x6NyX0c', '_score': 2.020018, '_source': {'title': 'Trembling of a Leaf, The', 'author': 'Maugham, William S', 'genere': 'fiction', 'sub-genere': 'novel', 'pages': '205', 'publisher': ''}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'u1m1CGEBztpV5x6Nv32R', '_score': 2.020018, '_source': {'title': 'We the Living', 'author': 'Rand, Ayn', 'genere': 'fiction', 'sub-genere': 'novel', 'pages': '178', 'publisher': 'Penguin'}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'cVm1CGEBztpV5x6NpH36', '_score': 2.020018, '_source': {'title': 'Veteran, The', 'author': 'Forsyth, Frederick', 'genere': 'fiction', 'sub-genere': 'novel', 'pages': '177', 'publisher': 'Transworld'}}]}}
========================================================================================================================================================================================================
 response4: {'took': 0, 'timed_out': False, '_shards': {'total': 5, 'successful': 5, 'skipped': 0, 'failed': 0}, 'hits': {'total': 77, 'max_score': 1.0890428, 'hits': [{'_index': 'book-5', '_type': 'book-map', '_id': 'jVm1CGEBztpV5x6Nrn3G', '_score': 1.0890428, '_source': {'title': 'Crime and Punishment', 'author': 'Dostoevsky, Fyodor', 'genere': 'fiction', 'sub-genere': 'classic', 'pages': '180', 'publisher': 'Penguin'}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'jlm1CGEBztpV5x6Nr30W', '_score': 1.0890428, '_source': {'title': 'Angels & Demons', 'author': 'Brown, Dan', 'genere': 'fiction', 'sub-genere': 'novel', 'pages': '178', 'publisher': 'Random House'}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'bFm1CGEBztpV5x6No31a', '_score': 1.0890428, '_source': {'title': 'Pillars of the Earth, The', 'author': 'Follett, Ken', 'genere': 'fiction', 'sub-genere': 'novel', 'pages': '176', 'publisher': 'Random House'}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'clm1CGEBztpV5x6NpX1S', '_score': 1.0890428, '_source': {'title': 'False Impressions', 'author': 'Archer, Jeffery', 'genere': 'fiction', 'sub-genere': 'novel', 'pages': '177', 'publisher': 'Pan'}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'e1m1CGEBztpV5x6NqH2f', '_score': 1.0890428, '_source': {'title': 'Asami Asami', 'author': 'Deshpande, P L', 'genere': 'fiction', 'sub-genere': 'novel', 'pages': '205', 'publisher': 'Mauj'}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'gVm1CGEBztpV5x6Nqn2T', '_score': 1.0890428, '_source': {'title': 'Catch 22', 'author': 'Heller, Joseph', 'genere': 'fiction', 'sub-genere': 'classic', 'pages': '178', 'publisher': 'Random House'}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'o1m1CGEBztpV5x6Ntn3R', '_score': 1.0890428, '_source': {'title': 'City of Joy, The', 'author': 'Lapierre, Dominique', 'genere': 'fiction', 'sub-genere': 'novel', 'pages': '177', 'publisher': 'vikas'}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'xVm1CGEBztpV5x6NxH3q', '_score': 1.0890428, '_source': {'title': 'Half A Life', 'author': 'Naipaul, V S', 'genere': 'fiction', 'sub-genere': 'novel', 'pages': '196', 'publisher': ''}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'tlm1CGEBztpV5x6NvX3U', '_score': 1.0890428, '_source': {'title': "Maugham's Collected Short Stories, Vol 3", 'author': 'Maugham, William S', 'genere': 'fiction', 'sub-genere': 'classic', 'pages': '171', 'publisher': 'Vintage'}}, {'_index': 'book-5', '_type': 'book-map', '_id': '21m1CGEBztpV5x6NzX2V', '_score': 1.0890428, '_source': {'title': 'Crisis on Infinite Earths', 'author': '', 'genere': 'fiction', 'sub-genere': 'comic', 'pages': '258', 'publisher': ''}}]}}
========================================================================================================================================================================================================
 response5: {'took': 0, 'timed_out': False, '_shards': {'total': 5, 'successful': 5, 'skipped': 0, 'failed': 0}, 'hits': {'total': 36, 'max_score': 2.1870723, 'hits': [{'_index': 'book-5', '_type': 'book-map', '_id': 'TVm1CGEBztpV5x6Nk33y', '_score': 2.1870723, '_source': {'title': 'Fundamentals of Wavelets', 'author': 'Goswami, Jaideva', 'genere': 'tech', 'sub-genere': 'signal_processing', 'pages': '228', 'publisher': 'Wiley'}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'ZFm1CGEBztpV5x6Nn33Z', '_score': 2.1870723, '_source': {'title': 'Signal and the Noise, The', 'author': 'Silver, Nate', 'genere': 'tech', 'sub-genere': 'data_science', 'pages': '233', 'publisher': 'Penguin'}}, {'_index': 'book-5', '_type': 'book-map', '_id': '01m1CGEBztpV5x6Nyn1j', '_score': 2.1870723, '_source': {'title': 'Pattern Classification', 'author': 'Duda, Hart', 'genere': 'tech', 'sub-genere': 'data_science', 'pages': '241', 'publisher': ''}}, {'_index': 'book-5', '_type': 'book-map', '_id': '-1m1CGEBztpV5x6N2X0-', '_score': 2.1870723, '_source': {'title': 'Design with OpAmps', 'author': 'Franco, Sergio', 'genere': 'tech', 'sub-genere': 'computer_science', 'pages': '240', 'publisher': ''}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'AVm1CGEBztpV5x6N236L', '_score': 2.1870723, '_source': {'title': 'Data Analysis with Open Source Tools', 'author': 'Janert, Phillip', 'genere': 'tech', 'sub-genere': 'data_science', 'pages': '230', 'publisher': ''}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'YVm1CGEBztpV5x6Nnn2X', '_score': 1.9588137, '_source': {'title': 'Making Software', 'author': 'Oram, Andy', 'genere': 'tech', 'sub-genere': 'computer_science', 'pages': '232', 'publisher': "O'Reilly"}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'Y1m1CGEBztpV5x6Nn31f', '_score': 1.9588137, '_source': {'title': 'Machine Learning for Hackers', 'author': 'Conway, Drew', 'genere': 'tech', 'sub-genere': 'data_science', 'pages': '233', 'publisher': "O'Reilly"}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'ZVm1CGEBztpV5x6NoH05', '_score': 1.9588137, '_source': {'title': 'Python for Data Analysis', 'author': 'McKinney, Wes', 'genere': 'tech', 'sub-genere': 'data_science', 'pages': '233', 'publisher': "O'Reilly"}}, {'_index': 'book-5', '_type': 'book-map', '_id': '6Vm1CGEBztpV5x6N0n26', '_score': 1.9588137, '_source': {'title': 'Power Electronics - Mohan', 'author': 'Mohan, Ned', 'genere': 'tech', 'sub-genere': 'computer_science', 'pages': '237', 'publisher': ''}}, {'_index': 'book-5', '_type': 'book-map', '_id': '7Vm1CGEBztpV5x6N0336', '_score': 1.9588137, '_source': {'title': 'Statistical Learning Theory', 'author': 'Vapnik, Vladimir', 'genere': 'tech', 'sub-genere': 'data_science', 'pages': '228', 'publisher': ''}}]}}
========================================================================================================================================================================================================
 response6: {'took': 0, 'timed_out': False, '_shards': {'total': 5, 'successful': 5, 'skipped': 0, 'failed': 0}, 'hits': {'total': 77, 'max_score': 1.0890428, 'hits': [{'_index': 'book-5', '_type': 'book-map', '_id': 'jVm1CGEBztpV5x6Nrn3G', '_score': 1.0890428, '_source': {'title': 'Crime and Punishment', 'author': 'Dostoevsky, Fyodor', 'genere': 'fiction', 'sub-genere': 'classic', 'pages': '180', 'publisher': 'Penguin'}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'jlm1CGEBztpV5x6Nr30W', '_score': 1.0890428, '_source': {'title': 'Angels & Demons', 'author': 'Brown, Dan', 'genere': 'fiction', 'sub-genere': 'novel', 'pages': '178', 'publisher': 'Random House'}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'bFm1CGEBztpV5x6No31a', '_score': 1.0890428, '_source': {'title': 'Pillars of the Earth, The', 'author': 'Follett, Ken', 'genere': 'fiction', 'sub-genere': 'novel', 'pages': '176', 'publisher': 'Random House'}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'clm1CGEBztpV5x6NpX1S', '_score': 1.0890428, '_source': {'title': 'False Impressions', 'author': 'Archer, Jeffery', 'genere': 'fiction', 'sub-genere': 'novel', 'pages': '177', 'publisher': 'Pan'}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'e1m1CGEBztpV5x6NqH2f', '_score': 1.0890428, '_source': {'title': 'Asami Asami', 'author': 'Deshpande, P L', 'genere': 'fiction', 'sub-genere': 'novel', 'pages': '205', 'publisher': 'Mauj'}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'gVm1CGEBztpV5x6Nqn2T', '_score': 1.0890428, '_source': {'title': 'Catch 22', 'author': 'Heller, Joseph', 'genere': 'fiction', 'sub-genere': 'classic', 'pages': '178', 'publisher': 'Random House'}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'o1m1CGEBztpV5x6Ntn3R', '_score': 1.0890428, '_source': {'title': 'City of Joy, The', 'author': 'Lapierre, Dominique', 'genere': 'fiction', 'sub-genere': 'novel', 'pages': '177', 'publisher': 'vikas'}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'xVm1CGEBztpV5x6NxH3q', '_score': 1.0890428, '_source': {'title': 'Half A Life', 'author': 'Naipaul, V S', 'genere': 'fiction', 'sub-genere': 'novel', 'pages': '196', 'publisher': ''}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'tlm1CGEBztpV5x6NvX3U', '_score': 1.0890428, '_source': {'title': "Maugham's Collected Short Stories, Vol 3", 'author': 'Maugham, William S', 'genere': 'fiction', 'sub-genere': 'classic', 'pages': '171', 'publisher': 'Vintage'}}, {'_index': 'book-5', '_type': 'book-map', '_id': '21m1CGEBztpV5x6NzX2V', '_score': 1.0890428, '_source': {'title': 'Crisis on Infinite Earths', 'author': '', 'genere': 'fiction', 'sub-genere': 'comic', 'pages': '258', 'publisher': ''}}]}}
========================================================================================================================================================================================================
 response7: {'took': 0, 'timed_out': False, '_shards': {'total': 5, 'successful': 5, 'skipped': 0, 'failed': 0}, 'hits': {'total': 2, 'max_score': 3.949246, 'hits': [{'_index': 'book-5', '_type': 'book-map', '_id': 'Y1m1CGEBztpV5x6Nn31f', '_score': 3.949246, '_source': {'title': 'Machine Learning for Hackers', 'author': 'Conway, Drew', 'genere': 'tech', 'sub-genere': 'data_science', 'pages': '233', 'publisher': "O'Reilly"}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'ZVm1CGEBztpV5x6NoH05', '_score': 3.949246, '_source': {'title': 'Python for Data Analysis', 'author': 'McKinney, Wes', 'genere': 'tech', 'sub-genere': 'data_science', 'pages': '233', 'publisher': "O'Reilly"}}]}}
========================================================================================================================================================================================================
 response8: {'took': 1, 'timed_out': False, '_shards': {'total': 5, 'successful': 5, 'skipped': 0, 'failed': 0}, 'hits': {'total': 0, 'max_score': None, 'hits': []}}
========================================================================================================================================================================================================
 response9: {'took': 1, 'timed_out': False, '_shards': {'total': 5, 'successful': 5, 'skipped': 0, 'failed': 0}, 'hits': {'total': 4, 'max_score': 4.6801376, 'hits': [{'_index': 'book-5', '_type': 'book-map', '_id': 'h1m1CGEBztpV5x6NrH29', '_score': 4.6801376, '_source': {'title': 'Learning OpenCV', 'author': 'Bradsky, Gary', 'genere': 'tech', 'sub-genere': 'signal_processing', 'pages': '232', 'publisher': "O'Reilly"}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'YVm1CGEBztpV5x6Nnn2X', '_score': 3.949246, '_source': {'title': 'Making Software', 'author': 'Oram, Andy', 'genere': 'tech', 'sub-genere': 'computer_science', 'pages': '232', 'publisher': "O'Reilly"}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'Y1m1CGEBztpV5x6Nn31f', '_score': 3.949246, '_source': {'title': 'Machine Learning for Hackers', 'author': 'Conway, Drew', 'genere': 'tech', 'sub-genere': 'data_science', 'pages': '233', 'publisher': "O'Reilly"}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'ZVm1CGEBztpV5x6NoH05', '_score': 3.949246, '_source': {'title': 'Python for Data Analysis', 'author': 'McKinney, Wes', 'genere': 'tech', 'sub-genere': 'data_science', 'pages': '233', 'publisher': "O'Reilly"}}]}}
========================================================================================================================================================================================================
 response10: {'took': 0, 'timed_out': False, '_shards': {'total': 5, 'successful': 5, 'skipped': 0, 'failed': 0}, 'hits': {'total': 0, 'max_score': None, 'hits': []}}
========================================================================================================================================================================================================
 response11: {'took': 0, 'timed_out': False, '_shards': {'total': 5, 'successful': 5, 'skipped': 0, 'failed': 0}, 'hits': {'total': 2, 'max_score': 6.2186866, 'hits': [{'_index': 'book-5', '_type': 'book-map', '_id': 'i1m1CGEBztpV5x6Nrn0c', '_score': 6.2186866, '_source': {'title': 'Let Us C', 'author': 'Kanetkar, Yashwant', 'genere': 'tech', 'sub-genere': 'computer_science', 'pages': '213', 'publisher': 'Prentice Hall'}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'iFm1CGEBztpV5x6NrX0h', '_score': 6.0042634, '_source': {'title': 'Data Structures Using C & C++', 'author': 'Tanenbaum, Andrew', 'genere': 'tech', 'sub-genere': 'computer_science', 'pages': '235', 'publisher': 'Prentice Hall'}}]}}
========================================================================================================================================================================================================
 response12: {'took': 0, 'timed_out': False, '_shards': {'total': 5, 'successful': 5, 'skipped': 0, 'failed': 0}, 'hits': {'total': 2, 'max_score': 6.2186866, 'hits': [{'_index': 'book-5', '_type': 'book-map', '_id': 'i1m1CGEBztpV5x6Nrn0c', '_score': 6.2186866, '_source': {'title': 'Let Us C', 'author': 'Kanetkar, Yashwant', 'genere': 'tech', 'sub-genere': 'computer_science', 'pages': '213', 'publisher': 'Prentice Hall'}}, {'_index': 'book-5', '_type': 'book-map', '_id': 'iFm1CGEBztpV5x6NrX0h', '_score': 6.0042634, '_source': {'title': 'Data Structures Using C & C++', 'author': 'Tanenbaum, Andrew', 'genere': 'tech', 'sub-genere': 'computer_science', 'pages': '235', 'publisher': 'Prentice Hall'}}]}}

E:\Vandan\DA-IICT\Academic Docs\Sem 2\IT562\Assignment 2> """
