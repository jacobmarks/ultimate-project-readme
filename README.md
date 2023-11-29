# Ultimate GitHub Project README

This is the Ultimate README Template for creating project READMEs. It is the Readme of Readmes! If you want to create a README for your project, this is the place to start.

## Table of Contents

- [Ultimate README Template](#ultimate-github-project-readme)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)
- [Tips and Tricks](#tips-and-tricks)
  - [Badges](#badges)
  - [GIFs](#gifs)
  - [Links](#links)
  - [Code Blocks](#code-blocks)
  - [Tables](#tables)
  - [Icons](#icons)

## Description

This is the place to describe your project. What does it do? Why did you make it? What problem does it solve? What did you learn? What challenges did you face? What are the technologies you used? What are the features? What are the future features? What is the status of the project? What is the roadmap? What is the license? What are the contributions guidelines? What are the test instructions? What is the contact information for the developer?

## 🚀 Installation

This is the place to describe how to install your project. What are the steps? What are the requirements? What are the dependencies? What is the order of the steps? What are the commands?

## Usage

This is the place to describe how to use your project. What are the steps? What are the commands? What are the options? What are the features? What are the examples? What are the screenshots? What are the GIFs?

## Contributing

This is the place to describe how to contribute to your project. What are the guidelines? What are the expectations? What are the steps? What are the commands? What are the requirements? What are the reccomendations? What are the resources? What is the code of conduct?

You can also include a [Contributing.md](./contributing.md) file in your repository. This will be displayed when someone creates a new issue or pull request.

### Contributors

It is also often helpful to include a listing of contributors in your README. You can do this manually, or you can use a tool like [Contrib.rocks](https://contrib.rocks/).

For instance, here is a list of contributors to the [FiftyOne](https://voxel51.com/fiftyone) project:

<a href="https://github.com/voxel51/fiftyone/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=voxel51/fiftyone" />
</a>

## License

This is the place to describe the license for your project. What are the terms? What are the limitations? What are the conditions? What are the permissions? What are the notices? What are the disclaimers? What are the badges?

# Tips and Tricks

## Badges

Badges are a great way to add some color and information to your README. Here are some great resources for badges:


<details>
<summary>Badge Resources (click to expand)</summary>

- [Shields.io](https://shields.io/)
- [Badge.fury.io](https://badge.fury.io/)
- [Badgen.net](https://badgen.net/)
- [Simpleicons.org](https://simpleicons.org/)
- [Dev.to](https://dev.to/envoy_/150-badges-for-github-pnk)
</details>

## GIFs

GIFs are a great way to add some life to your README. 

If you want to use an existing GIF, you can find some great options:

<details>
<summary>GIF Resources (click to expand)</summary>

- [Giphy](https://giphy.com/)
- [Gfycat](https://gfycat.com/)
- [Imgur](https://imgur.com/)
- [Tenor](https://tenor.com/)

</details>

Alternatively, you may want to record your own GIF. Here are some great tools for recording GIFs:

<details>
<summary>GIF Recording Tools (click to expand)</summary>

- [Giphy Capture](https://giphy.com/apps/giphycapture)
- [LICEcap](https://www.cockos.com/licecap/)
- [ScreenToGif](https://www.screentogif.com/)
- [Gifox](https://gifox.io/) *Paid, but very good*

</details>

### GIF Compression
Github allows you to embed GIFs in your README, **but** the maximum size is 10MB. If your GIF is larger than 10MB, you can use a tool like [XConvert](https://gfycat.com/) to compress it. You can also compress a GIF locally using [ffmpeg](https://ffmpeg.org/).

### Embedding GIFs

To embed a GIF in your README, simply drag and drop the GIF into the README in edit mode. Github will automatically upload the GIF and embed it in the README.

![gif_demo](https://github.com/jacobmarks/ultimate-project-readme/assets/12500356/e36b1273-460a-4852-946f-ac46f79f2cf7)

**Note:** You technically *can* use the markdown syntax to embed a GIF, but then the file will add to the size of your repository. If you drag and drop the GIF, it will be uploaded to Github's servers and will not add to the size of your repository.

### Encoding GIFs as Images

when you embed a GIF with the `.gif` extension in your README, you will need to press play to see the animation. If you want the GIF to animate automatically, you can encode it as an image with the `.png` extension. To do this, simply change the extension of the GIF from `.gif` to `.png`. This will cause the GIF to animate automatically!

Here's an example from the amazing [Tuana Çelik](https://github.com/TuanaCelik)!

![gif_demo](https://user-images.githubusercontent.com/15802862/220481971-ce7feeef-d5a3-4916-b8c3-feaf094e489f.png)

## Links

### Basic Links

You can add links to your README using the markdown syntax:

```md
[Link Text](https://www.example.com)
```

👉 [Link Text](https://www.example.com)

Alternatively, you can use HTML:

```html
<a href="https://www.example.com">Link Text</a>
```

👉 <a href="https://www.example.com">Link Text</a>

### Relative Links

You can also add relative links to your README using the syntax:

```md
[Relative Link Text](./path/to/file)
```

For instance, if you want to link to the [Contributing.md](./contributing.md) file in your repository, you can use the syntax:

```md
[Contributing](./contributing.md)
```

### Anchor Links

You can add anchor links to your README using the syntax:

```md
[Anchor Link Text](#anchor-name)
```

For instance, if you want to link to the [Installation](#installation) section of your README, you can use the syntax:

```md
[Installation](#installation)
```

**Note:** If your section header has emojis or special characters, you will need to **include them** in the anchor link. For instance, if you want to link to the [Installation](#🚀-installation) section of your README, you can would use the syntax:

```md
[Installation](#🚀-installation)
```


### Direct Links to Issues and Pull Requests

You can add direct links to issues and pull requests using the syntax:

```md
[Issue #num](https://github.com/user/repo/issues/num)
```

To link to [issue #1](https://github.com/jacobmarks/ultimate-project-readme/issues/1) in this repository, you can use the syntax:

```md
[Issue #1](https://github.com/jacobmarks/ultimate-project-readme/issues/1)
```

## Code Blocks

You can add code blocks to your README using the markdown syntax:

<pre>
```
print("Hello World!")
```
</pre>

👇

```
print("Hello World!")
```

### Syntax Highlighting

You can also add syntax highlighting to your code blocks by specifying the language:

#### Python

<pre>
```python
print("Hello World!")
```
</pre>

👇

```python
print("Hello World!")
```

#### JavaScript

<pre>
```javascript
console.log("Hello World!")
```
</pre>

👇

```javascript
console.log("Hello World!")
```


