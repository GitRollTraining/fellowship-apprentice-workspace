# Setup and maintenance

Dependencies for the caption route and the local transcription route, and the one recurring chore.

## Dependencies

| Tool | Caption route | Local transcription route | Install |
|---|---|---|---|
| `yt-dlp` | required | required, to fetch the media | `brew install yt-dlp` (macOS) · `pipx install yt-dlp` (anywhere) |
| `python3` | required | required | preinstalled on macOS and most Linux |
| `ffmpeg` | not used | required, to merge video and audio streams | `brew install ffmpeg` · `apt install ffmpeg` |

The cleaner uses the Python standard library only. There is nothing to `pip install`, and therefore
nothing to rot.

Confirm the install before using it in front of anyone:

```bash
yt-dlp --version && python3 --version
```

## No account, no key, no cost — on the caption route

The caption route reads a public captions track. It needs no account of any kind and no API key, which
is the reason it is the first route and not the fallback.

The local transcription route in `library/skills/video-to-markdown/` also needs no account: it
transcribes on this machine. Its own dependency notes are in that skill.

**If you ever use a hosted speech-to-text service instead**, two rules hold. It is your own account, and
the key belongs in the environment or in a gitignored `.env`, never in a committed file. And the owner's
recording leaves the machine, which is a decision the owner makes, not you.

## Permissions in this workspace

`.claude/settings.json` puts network commands behind an approval prompt, so the first `yt-dlp` call in a
session asks. That is deliberate — see `library/sops/agent-settings.md`. Approve it per session rather
than widening the rule.

## Maintenance — the one durability cost

Video sites periodically change their internals, which breaks `yt-dlp` roughly every quarter. Symptom:
the command errors on metadata or media fetch for a URL that plays fine in a browser.

```bash
brew upgrade yt-dlp     # or: pipx upgrade yt-dlp
```

Nothing else here rots. `ffmpeg` and the standard-library cleaner have been stable for years.

## Where the output goes

A transcript made from a client's video is that client's material:
`engagements/<client-slug>/interview/`, with the directory's `INDEX.md` updated in the same operation.
Anything you keep across clients — a question stem, a checking habit — is not client material and belongs
in `reference/`.

Keep the downloaded media out of the repository. Commit the transcript, not the recording.
