import { Injectable } from '@angular/core';
import { Headers, Http, Response, RequestOptions } from '@angular/http';

import 'rxjs/add/operator/toPromise';

import { Post } from './post';
import { POSTS } from './mock-posts';

@Injectable()
export class PostService {
    private postsUrl = '/api/v1/post/';

    constructor(private http: Http) { }

    getPosts(): Promise<Post[]> {
        return this.http.get(this.postsUrl)
                   .toPromise()
                   .then(this.extractData)
                   .catch(this.handleError);
    }

    private extractData(res: Response) {
        //response => response.json().data as Hero[]
        let body = res.json();
        return body.results || { };
    }


    private handleError(error: any): Promise<any> {
        console.error('An error occurred', error); // for demo purposes only
        return Promise.reject(error.message || error);
    }

    getPost(id: number): Promise<Post> {
        return this.getPosts().then(posts => posts.find(post => post.id === id));
    }
}