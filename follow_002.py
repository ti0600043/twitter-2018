# -*- coding: utf-8 -*-
import tweepy
import time
import datetime
import sys
import codecs

# python2系で起動するときは必要
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

def get_api():
    keys = dict(
        # 入力
        screen_name = 'biyo_kenko_net',
        consumer_key = 'VtjHUxPGeb0R7iST2IVdCiYk4',
        consumer_secret = 'IGdIQJOoF47hyE90F3DfEImXcjFQpGrUgf62oa8KUI4xdbh4oW',
        access_token =  '967363022132977665-SHgnMWdCqjDyRMHQ00lBG0fcUv6wQZO',
        access_token_secret = 'OD7phu8zzmy2RkSU0VoNfDg3kYkvhDmHUr2ERCPHtnU3j',
    )
 
    SCREEN_NAME = keys['screen_name']
    CONSUMER_KEY = keys['consumer_key']
    CONSUMER_SECRET = keys['consumer_secret']
    ACCESS_TOKEN = keys['access_token']
    ACCESS_TOKEN_SECRET = keys['access_token_secret']
 
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api, SCREEN_NAME
 
def unfollow(api, followers, friends):
    unfollow_cnt = 0
    for f in friends:
        if f not in followers:
            if unfollow_cnt <= 100:
               api.destroy_friendship(f)
               print(u"{0}のフォローを解除しました。".format(api.get_user(f).screen_name))
               time.sleep(2)
               unfollow_cnt += 1
            else:
                print(u'一度に解除可能な人数に達したため処理を中断します。')
                break
    return unfollow_cnt
 
def follow(copy_user, a_cnt):
	follow_cnt = 0
	# 検索ワードと追加フォロー数をセットし検索実行

	# フォロワーを取得
	search_results = api.followers_ids(copy_user)
	for result in search_results:
		if follow_cnt <= a_cnt:
			try:

				# screen_id = result.user._json["screen_name"]
				api.create_friendship(result)
				# api.create_friendship(screen_id)
				print(u"ID:{0}をフォローしました。".format(api.get_user(result).screen_name))
				# print(u"{0}をフォローしました。" .format(screen_id))
				time.sleep(2)
				follow_cnt += 1
			except tweepy.error.TweepError:
				print(u"フォローが失敗しました。")
	return follow_cnt
 
if __name__ == "__main__":

    # 日時を表示
    print(datetime.datetime.today())

    u_cnt = 0
    f_cnt = 0

    # 基本情報を取得
    api, SCREEN_NAME = get_api()
    followers = api.followers_ids(SCREEN_NAME)
    friends = api.friends_ids(SCREEN_NAME)
    u_cnt = unfollow(api, followers, friends)

    # 100回フォロー
    a_count = 100
    a_cnt = int(a_count)

    # 入力
    copy_user = "BeautyTrivia"
    
    f_cnt = follow(copy_user, a_cnt)
    print(u'{}人をフォロー解除、{}人をフォローしました。'.format(u_cnt,f_cnt))

    # 日時を表示
    print(datetime.datetime.today())
