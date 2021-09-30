{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f1e3c074",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\micha\\appdata\\local\\programs\\python\\python39\\lib\\site-packages\\facebook_scraper\\facebook_scraper.py:422: UserWarning: Locale detected as es_LA - for best results, set to en_US\n",
      "  warnings.warn(f\"Locale detected as {locale} - for best results, set to en_US\")\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "guardado exitosamente\n",
      "2\n",
      "guardado exitosamente\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\micha\\appdata\\local\\programs\\python\\python39\\lib\\site-packages\\facebook_scraper\\facebook_scraper.py:440: UserWarning: Facebook served mbasic/noscript content unexpectedly on https://m.facebook.com/page_content_list_view/more/?page_id=136319513087921&start_cursor=%7B%22timeline_cursor%22:%22AQHRsTsrFiUy6RkLQ62MKIx6bR_qwaUpbie_vB4sy7iMA6jLRlSTOUpKnS1WYuKm_45App4j7-r4o7JPoxbATw0beUci3EE-EGlAVJihHuV6owkxFYVDY1xT4pNMMJxK1jim%22,%22timeline_section_cursor%22:null,%22has_next_page%22:true%7D&num_to_fetch=4&surface_type=posts_tab\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "guardado exitosamente\n",
      "4\n",
      "guardado exitosamente\n",
      "5\n",
      "guardado exitosamente\n"
     ]
    }
   ],
   "source": [
    "from facebook_scraper import get_posts\n",
    "import couchdb\n",
    "import json\n",
    "import time\n",
    "\n",
    "couch=couchdb.Server('http://admin:admin@127.0.0.1:5984')\n",
    "server = couchdb.Server('http://admin:admin@127.0.0.1:5984')\n",
    "try:\n",
    "    db = server.create('autos')\n",
    "except:\n",
    "    db = server['autos']\n",
    "\n",
    "i=1\n",
    "for post in get_posts('autos', pages=1000, extra_info=True):\n",
    "    print(i)\n",
    "    i=i+1\n",
    "    time.sleep(5)\n",
    "    \n",
    "    id=post['post_id']\n",
    "    doc={}\n",
    "     \n",
    "    doc['id']=id\n",
    "    \n",
    "    mydate=post['time']\n",
    "    \n",
    "    try:\n",
    "        doc['texto']=post['text']\n",
    "        doc['date']=mydate.timestamp()\n",
    "        doc['likes']=post['likes']\n",
    "        doc['comments']=post['comments']\n",
    "        doc['shares']=post['shares']\n",
    "        try:\n",
    "            doc['reactions']=post['reactions']\n",
    "        except:\n",
    "            doc['reactions']={}\n",
    "\n",
    "        doc['post_url']=post['post_url']\n",
    "        db.save(doc)\n",
    "\n",
    "    \n",
    "        print(\"guardado exitosamente\")\n",
    "\n",
    "    except Exception as e:    \n",
    "        print(\"no se pudo grabar:\" + str(e))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f878960f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
