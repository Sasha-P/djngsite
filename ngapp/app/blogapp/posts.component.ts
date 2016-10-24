import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { Post } from './post';
import { PostService } from './post.service';

@Component({
    moduleId: module.id,
    selector: 'my-posts',
    templateUrl: 'posts.component.html',
    styleUrls: [ 'posts.component.css' ]
})
export class PostsComponent implements OnInit {
    posts: Post[];

    constructor(
        private router: Router,
        private postService: PostService
    ) { }

    getPosts(): void {
        this.postService.getPosts().then(posts => this.posts = posts);
    }

    ngOnInit(): void {
        this.getPosts();
    }

    gotoDetail(id): void {
        this.router.navigate(['/post', id]);
    }
}