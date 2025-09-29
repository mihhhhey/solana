from MyPools import *

NetworkList={
'solana':{'pages':10,'pages_trend':10,'vol_min':30000,'vol1h_min':1000,'tx_min':100,'cap_min':1,'lqty_min':1,'quotes':['solana_EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v','solana_So11111111111111111111111111111111111111112','solana_EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v'],
          'exclude':['solana_So11111111111111111111111111111111111111112','solana_Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB','solana_EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v','solana_JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN',
                     'solana_bSo13r4TkiE4KumL71LsHTPpL2euBYLFx6h9HP3piy1','solana_J1toso1uCk3RLmjorhTtrVwY9HJ7X8V9yYac6Y7kGCPn','solana_5oVNBeEEQvYi1cX3ir8Dx5n1P7pdxydbGF2X4TxVusJm','solana_mSoLzYCxHdYgdzU16g5QSh3i5K3z3KZK7ytfqcJm7So',
                     'solana_ukHH6c7mMyiWCf1b9pnWe25TSpkDDt3H5pQZgZ74J82','solana_5oVNBeEEQvYi1cX3ir8Dx5n1P7pdxydbGF2X4TxVusJm','solana_85VBFQZC9TZkfaptBWjvUw7YbZjy52A6mjtPGjstQAmQ','solana_7vfCXTUXx5WJV5JADk17DUJ4ksgau7utNKj4b963voxs',
                     'solana_3NZ9JMVBmGAqocybic2c7LQCJScmgsAZ6vQqTDzcqmJh','solana_HZ1JovNiVvGrGNiiYvEozEVgZ58xaU3RKwX8eACQBCt3','solana_4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R','solana_HhJpBhRRn4g56VsyLuT8DL5Bv31HkXqsrahTTUCZeZg4',
                     'solana_WENWENvqqNya429ubCdR81ZmD69brwQaaBYY6p3LCpk','solana_DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263','solana_ZEUS1aR7aX8DFFJf5QjWj2ftDDdNTroMNGo8YoQm3Gq','solana_A9mUU4qviSctJVPJdBJWkb28deg915LYJKrzQ19ji3FM',
                     'solana_rndrizKT3MK1iimdxRdWabcF7Zg7AR5T4nud4EkHBof','solana_jupSoLaHXQiZZTSfEWMTRRgpnyFm8f6sZdosWBjx93v','solana_EKpQGSJtjMFqKZ9KQanSqYXRcF8fBopzLHYxdM65zcjm','solana_7GCihgDB8fe6KNjn2MYtkzZcRjQy3t9GHdC8uHYmW2hr',
                     'solana_7BgBvyjrZX1YKz4oh9mjb8ZScatkkwb8DzFx7LoiVkM3','solana_5z3EqYQo9HiCEs3R84RCDMu2n7anpDMxRhdK8PSWmrRC','solana_25hAyBQfoDhfWx9ay6rarbgvWGwDdNqcHsXS3jQ3mTDJ','solana_MEW1gQWJ3nEXg2qgERiKu7FAFj79PHvQVREQUzScPP5',
                     'solana_2b1kV6DkPAnxd5ixfnxCpjxmKwqjjaYmCZfHsFu24GXo','solana_hntyVP6YFm1Hg25TN9WGLqM12b8TQmcknKrdu1oxWux','solana_sSo14endRuUbvQaJS3dq36Q829a3A6BEfoeeRGJywEh','solana_CLoUDKc4Ane7HeQcPpE3YHnznRxhMimJ4MyaUqyHFzAu',
                     'solana_CTJf74cTo3cw8acFP1YXF3QpsQUUBGBjh2k2e8xsZ6UL','solana_AujTJJ7aMS8LDo3bFzoyXDwT3jBALUbu4VZhzZdTZLmG','solana_ZEUS1aR7aX8DFFJf5QjWj2ftDDdNTroMNGo8YoQm3Gq','solana_Bybit2vBJGhPF52GBdNaQfUJ6ZpThSgHBobjWZpLPb4B',
                     'solana_GJAFwWjJ3vnTsrQVabjBVK2TYB1YtRCQXRDfDgUnpump','solana_2qEHjDLDLbuBgRYvsxhc5D6uDWAivNFZGan56P1tpump','solana_ED5nyyWEzpPPiWimP8vYm7sD7TD3LAt3Q3gRTWHzPJBY','solana_Bybit2vBJGhPF52GBdNaQfUJ6ZpThSgHBobjWZpLPb4B',]},
'ton':{'pages':3,'pages_trend':0,'vol_min':30000,'vol1h_min':1000,'tx_min':100,'cap_min':1,'lqty_min':1,'quotes':['ton_EQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM9c'],
       'exclude':['ton_EQBynBO23ywHy_CgarY9NK9FTz0yDsG82PtcbSTQgGoXwiuA','ton_EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs','ton_EQAJ8uWd7EBqsmpSWaRdf_I-8R8-XHwh3gsNKhy-UrdrPcUo','ton_EQCvxJy4eG8hyHBFsZ7eePxrRsUQSFE_jpptRAYBmcG_DOGS',
                  'ton_EQAvlWFDxGF2lXm67y4yzC17wYKD9A0guwPkMs1gOsM__NOT','ton_EQD-cvR0Nz6XAyRBvbhz-abTrRC6sI5tvHvvpeQraV9UAAD7',]},
'tron':{'pages':3,'pages_trend':0,'vol_min':30000,'vol1h_min':1000,'tx_min':100,'cap_min':1,'lqty_min':1,'quotes':['tron_TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t','tron_TNUC9Qb1rRpS5CbWLmNMxXBjyFoydXjWFR'],
       'exclude':['tron_TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t','tron_TNUC9Qb1rRpS5CbWLmNMxXBjyFoydXjWFR','tron_TN3W4H6rK2ce4vX9YnFQHwKENnHjoxb3m9','tron_TSSMHYeV2uE9qYH95DqyoCuNCzEL1NvU3S','tron_TRFe3hT5oYhjSZ6f3ji5FJ7YCfrkWnHRvh',
                  'tron_TCFLL5dx5ZJdKnWuesXxi1VPwjLVmWZZy9',]},
'sui-network':{'pages':3,'pages_trend':0,'vol_min':30000,'vol1h_min':1000,'tx_min':100,'cap_min':1,'lqty_min':1,'quotes':['sui-network_0x2::sui::SUI','sui-network_0x5d4b302506645c37ff133b98c4b50a5ae14841659738d6d733d59d0d217a93bf::coin::COIN','sui-network_0xdba34672e30cb065b1f93e3ab55318768fd6fef66c15942c9f7cb846e2f900e7::usdc::USDC'],
       'exclude':['sui-network_0x2::sui::SUI','sui-network_0xdba34672e30cb065b1f93e3ab55318768fd6fef66c15942c9f7cb846e2f900e7::usdc::USDC','sui-network_0xc060006111016b8a020ad5b33834984a437aaa7d3c74c18e09a95d48aceab08c::coin::COIN',
                  'sui-network_0x6864a6f921804860930db6ddbe2e16acdf8504495ea7481637a1c8b9a8fe54b::cetus::CETUS','sui-network_0xaf8cd5edc19c4512f4259f0bee101a40d41ebed738ade5874359610ef8eeced5::coin::COIN',
                  'sui-network_0xbde4ba4c2e274a60ce15c1cfff9e5c42e41654ac8b6d906a57efa4bd3c29f47d::hasui::HASUI','sui-network_0x549e8b69270defbfafd4f94e17ec44cdbdd99820b33bda2278dea3b9a32d3f55::cert::CERT',
                  'sui-network_0xb7844e289a8410e50fb3ca48d69eb9cf29e27d223ef90353fe1bd8e27ff8f3f8::coin::COIN','sui-network_0x27792d9fed7f9844eb4839566001bb6f6cb4804f66aa2da6fe1ee242d896881::coin::COIN',
                  'sui-network_0xce7ff77a83ea0cb6fd39bd8748e2ec89a3f41e8efdc3f4eb123e0ca37b184db2::buck::BUCK']},
'bsc':{'pages':3,'pages_trend':3,'vol_min':30000,'vol1h_min':1000,'tx_min':100,'cap_min':1,'lqty_min':1,'quotes':['bsc_0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c','bsc_0x55d398326f99059ff775485246999027b3197955'],
       'exclude':[]},
}

if __name__ == "__main__":
    from geckodex_api import *
    networks=['solana','tron','ton','sui-network']
    networks=['solana']
    networks=['solana','bsc']
    Pools=UpdatePools(networks,add=0,p=0)
    now=int(time.time())
    #print(Pools)
    for network in Pools:
        print('\n',network)
        for el in Pools[network]:
            print(el['name'],el['vol24h'],el['vol1h'],el['change'],(now-el['timestamp'])//86400)
