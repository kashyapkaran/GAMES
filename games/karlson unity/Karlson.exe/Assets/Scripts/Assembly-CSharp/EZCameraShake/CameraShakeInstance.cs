using UnityEngine;

namespace EZCameraShake
{
	public class CameraShakeInstance
	{
		public CameraShakeInstance(float magnitude, float roughness)
		{
		}

		public float Magnitude;
		public float Roughness;
		public Vector3 PositionInfluence;
		public Vector3 RotationInfluence;
		public bool DeleteOnInactive;
	}
}
