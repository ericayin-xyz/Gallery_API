from controllers.gallery_controller import galleries
from controllers.auth_controller import auth
from controllers.artist_controller import artists
from controllers.artwork_controller import artworks
from controllers.exhibition_controller import exhibitions


registerable_controllers = [
    galleries, auth, artists, artworks, exhibitions
]