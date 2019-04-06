"""A Yelp-powered Restaurant Recommendation Program"""

from abstractions import *
from data import ALL_RESTAURANTS, CATEGORIES, USER_FILES, load_user_file
from ucb import main, trace, interact
from utils import distance, mean, zip, enumerate, sample
from visualize import draw_map

##################################
# Phase 2: Unsupervised Learning #
##################################


def find_closest(location, centroids):
    """Return the centroid in centroids that is closest to location.
    If multiple centroids are equally close, return the first one.

    >>> find_closest([3.0, 4.0], [[0.0, 0.0], [2.0, 3.0], [4.0, 3.0], [5.0, 5.0]])
    [2.0, 3.0]
    """
    # BEGIN Question 3
    # My solution:
    for k in centroids:
        if distance(location,k)==min([distance(location,i)for i in centroids]):
            return k
    # czahie from github
    """
    closest_centroid = min(centroids, key=lambda centroid: distance(location, centroid))
    return closest_centroid
    """

def group_by_first(pairs):
    """Return a list of lists that relates each unique key in the [key, value]
    pairs to a list of all values that appear paired with that key.

    Arguments:
    pairs -- a sequence of pairs

    >>> example = [ [1, 2], [3, 2], [2, 4], [1, 3], [3, 1], [1, 2] ]
    >>> group_by_first(example)  # Values from pairs that start with 1, 3, and 2 respectively
    [[2, 3, 2], [2, 1], [4]]
    """
    keys = []
    for key, _ in pairs:
        if key not in keys:
            keys.append(key)
    return [[y for x, y in pairs if x == key] for key in keys]


def group_by_centroid(restaurants, centroids):
    """Return a list of clusters, where each cluster contains all restaurants
    nearest to a corresponding centroid in centroids. Each item in
    restaurants should appear once in the result, along with the other
    restaurants closest to the same centroid.
    """
    # BEGIN Question 4
    return group_by_first([[find_closest(restaurant_location(restaurant),centroids),restaurant] for restaurant in restaurants ])
    # END Question 4


def find_centroid(cluster):
    """Return the centroid of the locations of the restaurants in cluster."""
    # BEGIN Question 5
    return [mean([restaurant_location(r)[0] for r in cluster]),mean([restaurant_location(r)[1] for r in cluster])]
    #This may not prefect
    # END Question 5


def k_means(restaurants, k, max_updates=100):
    """Use k-means to group restaurants by location into k clusters."""
    assert len(restaurants) >= k, 'Not enough restaurants to cluster'
    old_centroids, n = [], 0

    # Select initial centroids randomly by choosing k different restaurants
    centroids = [restaurant_location(r) for r in sample(restaurants, k)]

    while old_centroids != centroids and n < max_updates:
        old_centroids = centroids
        # BEGIN Question 6
        centroids=[find_centroid(i) for i in group_by_centroid(restaurants,centroids)]
        # END Question 6
        n += 1
    return centroids


################################
# Phase 3: Supervised Learning #
################################

from math import sqrt
def find_predictor(user, restaurants, feature_fn):
    """Return a rating predictor (a function from restaurants to ratings),
    for a user by performing least-squares linear regression using feature_fn
    on the items in restaurants. Also, return the R^2 value of this model.

    Arguments:
    user -- A user
    restaurants -- A sequence of restaurants
    feature_fn -- A function that takes a restaurant and returns a number
    """
    xs = [feature_fn(r) for r in restaurants]
    ys = [user_rating(user, restaurant_name(r)) for r in restaurants]

    # BEGIN Question 7

    mean_xs=mean(xs)
    mean_ys=mean(ys)
    S_xx=sum([(x_i-mean_xs)**2 for x_i in xs])
    S_yy=sum([(y_i-mean_ys)**2 for y_i in ys])
    # My first solution
    # When I wrote this ,only God and I can know what I was doing
    # Now ,God only knows
    """
    S_xy=0
    for i in range(len(xs)):
        S_xy+=(xs[i]-mean_xs)*(ys[i]-mean_ys)
    """

    # My second solution
    S_xy=sum([(x_i-mean_xs)*(y_i-mean_ys) for x_i,y_i in zip(xs,ys)])
    b=S_xy/S_xx
    a=mean_ys-b*mean_xs
    r_squared=S_xy**2/(S_xx*S_yy)
    # END Question 7
    """
    pairs = zip(xs, ys)
    s_xx, s_yy, s_xy = 0, 0, 0
    for x, y in pairs:
        s_xx += (x - mean(xs)) ** 2
        s_yy += (y - mean(ys)) ** 2
        s_xy += (x - mean(xs)) * (y - mean(ys))
    b = s_xy / s_xx
    a = mean(ys) - b * mean(xs)
    r_squared = (s_xy ** 2) / (s_xx * s_yy)
    """
    def predictor(restaurant):
        return b * feature_fn(restaurant) + a

    return predictor, r_squared
    # Error: expected
    #     0.99256
    # but got
    #     0.99627

    # czahie from github


def best_predictor(user, restaurants, feature_fns):
    """Find the feature within feature_fns that gives the highest R^2 value
    for predicting ratings by the user; return a predictor using that feature.

    Arguments:
    user -- A user
    restaurants -- A list of restaurants
    feature_fns -- A sequence of functions that each takes a restaurant
    """
    reviewed = user_reviewed_restaurants(user, restaurants)
    # BEGIN Question 8
    predictor_r_square=[list(find_predictor(user,reviewed,feature_fn)) for feature_fn in feature_fns]
    best_return_list=max(predictor_r_square,key=lambda x:x[1])
    return best_return_list[0]    #It is magic ,don't touch it !
    # END Question 8
    """
    # czahie's solution from github
    predictors = {find_predictor(user, reviewed, feature_fn)[0]: find_predictor(user, reviewed, feature_fn)[1]
                  for feature_fn in feature_fns}
    return max(predictors, key=lambda key: predictors[key])
    """

def rate_all(user, restaurants, feature_fns):
    """Return the predicted ratings of restaurants by user using the best
    predictor based on a function from feature_fns.

    Arguments:
    user -- A user
    restaurants -- A list of restaurants
    feature_fns -- A sequence of feature functions
    """
    predictor = best_predictor(user, ALL_RESTAURANTS, feature_fns)
    reviewed = user_reviewed_restaurants(user, restaurants)
    # BEGIN Question 9
    final_dict={}
    for restaurant in restaurants:
        if restaurant in reviewed:
            final_dict[restaurant_name(restaurant)]= user_rating(user,restaurant_name(restaurant))
        else :
            final_dict[restaurant_name(restaurant)]= predictor(restaurant)
    return final_dict
    # END Question 9
    """ czahie's solution from github
    a little more beautiful
    all_restaurant = {}
    for restaurant in restaurants:
        name = restaurant_name(restaurant)
        if restaurant in reviewed:
            all_restaurant[name] = user_rating(user, name)
        else:
            all_restaurant[name] = predictor(restaurant)
    return all_restaurant
    """


def search(query, restaurants):
    """Return each restaurant in restaurants that has query as a category.

    Arguments:
    query -- A string
    restaurants -- A sequence of restaurants
    """
    # BEGIN Question 10
    return [restaurant for restaurant in restaurants if query in restaurant_categories(restaurant)]   # It's magic ,don't touch it
    # END Question 10


def feature_set():
    """Return a sequence of feature functions."""
    return [lambda r: mean(restaurant_ratings(r)),
            restaurant_price,
            lambda r: len(restaurant_ratings(r)),
            lambda r: restaurant_location(r)[0],
            lambda r: restaurant_location(r)[1]]


@main
def main(*args):
    import argparse
    parser = argparse.ArgumentParser(
        description='Run Recommendations',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('-u', '--user', type=str, choices=USER_FILES,
                        default='test_user',
                        metavar='USER',
                        help='user file, e.g.\n' +
                        '{{{}}}'.format(','.join(sample(USER_FILES, 3))))
    parser.add_argument('-k', '--k', type=int, help='for k-means')
    parser.add_argument('-q', '--query', choices=CATEGORIES,
                        metavar='QUERY',
                        help='search for restaurants by category e.g.\n'
                        '{{{}}}'.format(','.join(sample(CATEGORIES, 3))))
    parser.add_argument('-p', '--predict', action='store_true',
                        help='predict ratings for all restaurants')
    parser.add_argument('-r', '--restaurants', action='store_true',
                        help='outputs a list of restaurant names')
    args = parser.parse_args()

    # Output a list of restaurant names
    if args.restaurants:
        print('Restaurant names:')
        for restaurant in sorted(ALL_RESTAURANTS, key=restaurant_name):
            print(repr(restaurant_name(restaurant)))
        exit(0)

    # Select restaurants using a category query
    if args.query:
        restaurants = search(args.query, ALL_RESTAURANTS)
    else:
        restaurants = ALL_RESTAURANTS

    # Load a user
    assert args.user, 'A --user is required to draw a map'
    user = load_user_file('{}.dat'.format(args.user))

    # Collect ratings
    if args.predict:
        ratings = rate_all(user, restaurants, feature_set())
    else:
        restaurants = user_reviewed_restaurants(user, restaurants)
        names = [restaurant_name(r) for r in restaurants]
        ratings = {name: user_rating(user, name) for name in names}

    # Draw the visualization
    if args.k:
        centroids = k_means(restaurants, min(args.k, len(restaurants)))
    else:
        centroids = [restaurant_location(r) for r in restaurants]
    draw_map(centroids, restaurants, ratings)
