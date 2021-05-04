using System;
using UnityEngine;

namespace Audio
{
	[Serializable]
	public class Sound
	{
		public string name;
		public AudioClip clip;
		public float volume;
		public float pitch;
		public bool loop;
		public bool bypass;
		public AudioSource source;
	}
}
