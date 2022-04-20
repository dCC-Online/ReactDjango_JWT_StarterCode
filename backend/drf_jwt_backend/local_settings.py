# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g@02@8x89*loc1tmyc_jq(op9mzv1x((kp-^kddyha(qgcp^nl'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'react_django_starter',
        'USER': 'root',
        'PASSWORD': 'R@diohead97',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
