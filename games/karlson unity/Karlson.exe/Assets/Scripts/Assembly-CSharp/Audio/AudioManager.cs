using UnityEngine;

namespace Audio
{
	public class AudioManager : MonoBehaviour
	{
		public Sound[] sounds;
		public Sound[] footsteps;
		public Sound[] wallrun;
		public Sound[] jumps;
		public AudioLowPassFilter filter;
		public bool muted;
	}
}
