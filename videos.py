import csv
import pprint


def get_video_data():
    """this function reads from a .csv file and converts the data into a list of dictionaries.
     each item in the list is a dictionary of a specific videos and their attributes."""

    vid_data = []
    with open('USvideos.csv', newline='', encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            if len(row) == 16:
                vid_dict = {'video_id': row[0],
                            'trending_date': row[1],
                            'title': row[2],
                            'channel_title': row[3],
                            'category_id': row[4],
                            'publish_times': row[5],
                            'tags': row[6],
                            'views': row[7],
                            'likes': row[8],
                            'dislikes': row[9],
                            'comment_count': row[10],
                            'thumbnail_link': row[11],
                            'comments_disabled': row[12],
                            'ratings_disabled': row[13],
                            'video_error': row[14],
                            'description': row[15]
                            }
                vid_data.append(vid_dict)
    return vid_data


def print_data(data):
    for entry in data:
        pprint.pprint(entry)


def get_most_popular_and_least_popular_channel(data):
    """ fill in the Nones for the dictionary below using the vid data """
    most_popular_and_least_popular_channel = {'most_popular_channel': None, 'least_popular_channel': None,
                                              'most_pop_num_views': None, 'least_pop_num_views': None}
    channel_list_views = {}

    for item in data[1:]:
        channel_list_views.setdefault(item['channel_title'], 0)
        channel_list_views[item['channel_title']] += int(item['views'])

    popular_dict = {'channel_title': None, 'views': 0}
    for k, v in channel_list_views.items():
        if int(v) > popular_dict['views']:
            popular_dict['channel_title'] = k
            popular_dict['views'] = int(v)
        most_popular_and_least_popular_channel['most_popular_channel'] = popular_dict['channel_title']
        most_popular_and_least_popular_channel['most_pop_num_views'] = popular_dict['views']

    not_popular_dict = {'channel_title': None, 'views': float('Inf')}
    for k, v in channel_list_views.items():
        if int(v) < not_popular_dict['views']:
            not_popular_dict['channel_title'] = k
            not_popular_dict['views'] = int(v)
        most_popular_and_least_popular_channel['least_popular_channel'] = not_popular_dict['channel_title']
        most_popular_and_least_popular_channel['least_pop_num_views'] = not_popular_dict['views']
    return most_popular_and_least_popular_channel


def get_most_liked_and_disliked_channel(data):
    """ fill in the Nones for the dictionary below using the bar party data """

    most_liked_and_disliked_channel = {'most_liked_channel': None, 'num_likes': None,
                                       'most_disliked_channel': None, 'num_dislikes': None}

    channel_likes = {}
    channel_dislikes = {}

    for item in data[1:]:
        channel_likes.setdefault(item['channel_title'], 0)
        channel_dislikes.setdefault(item['channel_title'], 0)
        channel_likes[item['channel_title']] += int(item['likes'])
        channel_dislikes[item['channel_title']] += int(item['dislikes'])

    likes_dict = {'channel_title': None, 'likes': 0}
    for k, v in channel_likes.items():
        if int(v) > likes_dict['likes']:
            likes_dict['channel_title'] = k
            likes_dict['likes'] = int(v)
        most_liked_and_disliked_channel['most_liked_channel'] = likes_dict['channel_title']
        most_liked_and_disliked_channel['num_likes'] = likes_dict['likes']

    dislikes_dict = {'channel_title': None, 'dislikes': 0}
    for k, v in channel_dislikes.items():
        if int(v) > dislikes_dict['dislikes']:
            dislikes_dict['channel_title'] = k
            dislikes_dict['dislikes'] = int(v)
        most_liked_and_disliked_channel['most_disliked_channel'] = dislikes_dict['channel_title']
        most_liked_and_disliked_channel['num_dislikes'] = dislikes_dict['dislikes']
    return most_liked_and_disliked_channel


if __name__ == '__main__':
    vid_data = get_video_data()

    # uncomment the line below to see what the data looks like
    # print_data(vid_data)

    popularity_metrics = get_most_popular_and_least_popular_channel(vid_data)

    like_dislike_metrics = get_most_liked_and_disliked_channel(vid_data)

    print('Popularity Metrics: {}'.format(popularity_metrics))
    print('Like Dislike Metrics: {}'.format(like_dislike_metrics))
